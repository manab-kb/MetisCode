import os
import sys
import re
import json
import openai
import unittest
from flask import Flask, request, jsonify
import argparse
# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from Backend.hint_system.code_analyzer import CodeAnalyzer

class AdaptiveHintGenerator:
    def __init__(self, questions_path):
        with open(questions_path, 'r', encoding='utf-8') as f:
            self.questions = json.load(f)
        self.analyzers = {
            q['question_name']: CodeAnalyzer(problem_keywords=self._extract_keywords(q['question'])) 
            for q in self.questions
        }
        self.rules = self._load_rules()
    
    def _extract_keywords(self, question_text):
        return list(set(re.findall(r'\b(\w+)\b', question_text.lower())))
    
    def _load_rules(self):
        from question_rules import QUESTION_HINT_RULES
        return QUESTION_HINT_RULES
    
    def generate_hints(self, question_name, user_code):
        question = next(q for q in self.questions if q['question_name'] == question_name)
        analyzer = self.analyzers[question_name]
        
        ast = analyzer.parse_ast(user_code)
        if isinstance(ast, dict):
            return [{"hint": f"Syntax Error: {ast['error']}", "type": "syntax"}]
        
        issues = analyzer.find_issues(ast)
        context = analyzer.analyze_problem_context(user_code)
        
        hints = []
        hints += self._apply_question_rules(question_name, user_code, issues)
        hints += [{"hint": issue, "type": "general"} for issue in issues]
        #hints += self._constraint_hints(question)

        print(len(hints))
        if len(hints) < 2:
            print("test")
            for i, hint in enumerate(hints, 1):
                print(f"Hint before {i}: [{hint['type']}] {hint['hint']}")   
            llm_hint = self._generate_llm_hint(question, user_code, issues, context)
            hints.append(llm_hint)
            for i, hint in enumerate(hints, 1):
                print(f"Hint after {i}: [{hint['type']}] {hint['hint']}")            
        return hints[:3]

    def _generate_llm_hint(self, question, user_code, issues, context):
        try:
            prompt = f"""**Problem**: {question['question']}
            **Constraints**: {', '.join(question['constraints'])}
            **Student Code**: {user_code}
            **Detected Issues**: {', '.join(issues)}
            **Missing Concepts**: {', '.join(context['missing_concepts'])}"""
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "system",
                    "content": "Generate a helpful programming hint that: "
                               "1. Identifies one core misunderstanding "
                               "2. Suggests an approach without direct code "
                               "3. Asks a guiding question"
                }, {
                    "role": "user", 
                    "content": prompt
                }],
                temperature=0.4,
                max_tokens=150
            )
            
            return {
                "hint": response.choices[0].message.content,
                "type": "llm",
                "confidence": 0.7
            }
        except Exception:
            return {
                "hint": "Break the problem into smaller steps and validate each part",
                "type": "fallback",
                "confidence": 0.5
            }

    def _apply_question_rules(self, question_name, code, issues):
        hints = []
        for rule in self.rules.get(question_name, []):
            if any(re.search(p, code, re.DOTALL) for p in rule['patterns']):
                hints.extend({
                    "hint": h,
                    "type": "question-specific",
                    "trigger": rule['trigger']
                } for h in rule['hints'])
        return hints
    
    def _constraint_hints(self, question):
        return [
            {"hint": hint, "type": "constraint"}
            for constraint in question['constraints']
            for hint in self._get_constraint_hint(constraint)
        ]
    
    def _get_constraint_hint(self, constraint):
        constraint_hints = {
            "O(1) space": "Try to modify values in-place instead of creating new data structures",
            "without using division": "Consider using prefix and suffix product arrays",
            "O(n) time complexity": "Avoid nested loops, consider using a hash map or sliding window",
            "in-place": "Modify the input directly rather than creating new structures"
        }
        return [constraint_hints.get(constraint, f"Consider the constraint: {constraint}")]


    # ================== JSON File Output ==================
    def save_hints_to_json(hints_data, filename="hints_output.json"):
        with open(filename, 'w') as f:
            json.dump(hints_data, f, indent=2)
        print(f"\nHints saved to {filename}")

        # ================== Flask API Setup ==================
    app = Flask(__name__)
    generator = None  # Will be initialized during app startup

    @app.route('/hints', methods=['POST'])
    def generate_hints_api():
        try:
            data = request.get_json()
            question_name = data['question_name']
            user_code = data['code']
            
            hints = generator.generate_hints(question_name, user_code)
            return jsonify({
                "question": question_name,
                "hints": hints,
                "status": "success"
            }), 200
            
        except Exception as e:
            return jsonify({
                "error": str(e),
                "status": "error"
            }), 400

class TestHintSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cls.questions_path = os.path.join(current_dir, "questions.json")
        cls.sample_code_dir = os.path.join(current_dir, "tests", "sample_code")
        
        with open(cls.questions_path) as f:
            cls.questions = {q['question_name']: q for q in json.load(f)}

        cls.generator = AdaptiveHintGenerator(
            cls.questions_path
        )

    def test_all_questions(self):
        """Test all sample files against corresponding questions"""
        for filename in os.listdir(self.sample_code_dir):
            if not filename.endswith("_buggy.py"):
                continue
                
            with self.subTest(question=filename):
                # Convert filename to question name
                base_name = filename.replace("_buggy.py", "")
                question_name = ' '.join([word.capitalize() for word in base_name.split('_')])
                
                # Handle special naming conventions
                question_name = next(
                    (qname for qname in self.questions if qname.lower() == question_name.lower()),
                    None
                )
                
                if not question_name:
                    self.fail(f"No matching question found for file: {filename}")
                
                file_path = os.path.join(self.sample_code_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read().strip()
                
                if not code:
                    self.fail(f"Empty test file: {filename}")
                
                hints = self.generator.generate_hints(question_name, code)
                
                print(f"\n\n=== Results for {filename} ===")
                print(f"Question: {question_name}")
                for i, hint in enumerate(hints, 1):
                    print(f"Hint {i}: [{hint['type']}] {hint['hint']}")
                
                self.assertGreater(len(hints), 0, f"No hints generated for {filename}")


# ========== Flask API Setup ==========
app = Flask(__name__)
generator = None

@app.route('/hints', methods=['POST'])
def generate_hints():
    try:
        data = request.get_json()
        required_fields = ['question_name', 'code']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        response_data = {
            "question": data['question_name'],
            "hints": generator.generate_hints(data['question_name'], data['code']),
            "status": "success"
        }
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

# ========== Startup Configuration ==========
def create_app():
    global generator
    questions_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        "questions.json"
    )
    
    generator = AdaptiveHintGenerator(
        questions_path)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

