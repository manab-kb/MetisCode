# # import os
# # import sys
# # import re
# # import json
# # import unittest

# # # Add project root to Python path
# # project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # sys.path.insert(0, project_root)

# # from app.hint_system.code_analyzer import CodeAnalyzer

# # class AdaptiveHintGenerator:
# #     def __init__(self, questions_path):
# #         try:
# #             with open(questions_path, 'r', encoding='utf-8') as f:
# #                 self.questions = json.load(f)
# #         except FileNotFoundError:
# #             raise ValueError(f"Questions file not found at {questions_path}")
# #         except json.JSONDecodeError:
# #             raise ValueError("Invalid JSON format in questions file")
        
# #         self.analyzers = {
# #             q['question_name']: CodeAnalyzer() 
# #             for q in self.questions
# #         }
        
# #         self.rules = self._load_rules()
    
# #     def _load_rules(self):
# #         from question_rules import QUESTION_HINT_RULES
        
# #         print("\n=== DEBUG: LOADED RULES ===")
# #         for q_name, rules in QUESTION_HINT_RULES.items():
# #             print(f"\nQuestion: {q_name}")
# #             for i, rule in enumerate(rules, 1):
# #                 print(f"  Rule {i}:")
# #                 print(f"    Trigger: {rule.get('trigger', 'MISSING')}")
# #                 print(f"    Patterns: {rule.get('patterns', 'MISSING')}")
# #                 print(f"    Hints: {rule.get('hints', 'MISSING')}")
        
# #         # Validation (now runs AFTER safe debug print)
# #         for q_name, rules in QUESTION_HINT_RULES.items():
# #             for rule in rules:
# #                 if 'patterns' not in rule:
# #                     raise ValueError(f"Rule for {q_name} missing 'patterns' key")
# #                 if not isinstance(rule['patterns'], list):
# #                     raise ValueError(f"Patterns must be list in {q_name}")
        
# #         return QUESTION_HINT_RULES
    
# #     def generate_hints(self, question_name, user_code):
# #         question = next(q for q in self.questions if q['question_name'] == question_name)
# #         analyzer = self.analyzers[question_name]
        
# #         ast = analyzer.parse_ast(user_code)
# #         if isinstance(ast, dict):
# #             return [{"hint": f"Syntax Error: {ast['error']}", "type": "syntax"}]
        
# #         issues = analyzer.find_issues(ast)
# #         hints = []
# #         hints += self._apply_question_rules(question_name, user_code, issues)
# #         hints += self._constraint_hints(question)
# #         hints += [{"hint": issue, "type": "general"} for issue in issues]
        
# #         return hints[:3]

# #     # def _apply_question_rules(self, question_name, code, issues):
# #     #     hints = []
# #     #     for rule in self.rules.get(question_name, []):
# #     #         patterns = rule.get('patterns', [])
# #     #         if not isinstance(patterns, list):
# #     #             continue
# #     #         if any(re.search(p, code) for p in patterns):
# #     #             hints.extend({
# #     #                 "hint": h,
# #     #                 "type": "question-specific",
# #     #                 "triggers": rule.get('trigger', 'unknown')
# #     #             } for h in rule.get('hints', []))
# #     #     return hints
# #     def _apply_question_rules(self, question_name, code, issues):
# #         hints = []
# #         print(f"\n=== RAW CODE FOR {question_name} ===\n{code}\n=== END RAW CODE ===")
        
# #         for rule in self.rules.get(question_name, []):
# #             print(f"\nChecking rule: {rule['trigger']}")
# #             for pattern in rule['patterns']:
# #                 print(f"Testing pattern: {pattern}")
# #                 if re.search(pattern, code, re.DOTALL):
# #                     print("MATCH FOUND!")
# #                     hints.extend({
# #                         "hint": h,
# #                         "type": "question-specific",
# #                         "triggers": rule['trigger']
# #                     } for h in rule['hints'])
# #                     break
# #         return hints
    
# #     def _constraint_hints(self, question):
# #         hints = []
# #         constraints = "\n".join(question['constraints'])
        
# #         if "O(1) space" in constraints:
# #             hints.append({"hint": "Try to solve this with constant extra space", "type": "constraint"})
# #         if "without using division" in constraints:
# #             hints.append({"hint": "Use prefix and suffix product arrays", "type": "constraint"})
        
# #         return hints

# # class TestHintSystem(unittest.TestCase):
# #     @classmethod
# #     def setUpClass(cls):
# #         current_dir = os.path.dirname(os.path.abspath(__file__))
# #         questions_path = os.path.join(current_dir, "questions.json")
# #         cls.generator = AdaptiveHintGenerator(questions_path)
    
# #     def test_can_place_flowers(self):
# #         current_dir = os.path.dirname(os.path.abspath(__file__))
# #         sample_path = os.path.join(current_dir, "tests", "sample_code", "can_place_flowers_buggy.py")
# #         with open(sample_path) as f:
# #             code = f.read()
            
# #         hints = self.generator.generate_hints("Can Place Flowers", code)
# #         self.assertGreater(len(hints), 0)
# #         print("\nCan Place Flowers Hints:")
# #         for h in hints: print(f"- {h['hint']}")
# #     # Buggy implementation that will trigger our new rules
# #     # def reverseVowels(s):
# #     #     vowels = 'aeiou'  # Should include uppercase
# #     #     return ''.join([c for c in s if c in vowels][::-1] + [c for c in s if c not in vowels])
# #     def reverseVowels(s):
# #         vowels = 'aeiou'  # Missing uppercase vowels
# #         return ''.join([c for c in s if c in vowels][::-1])  # Incorrect reversal
    

# #     def test_reverse_vowels(self):
# #         current_dir = os.path.dirname(os.path.abspath(__file__))
# #         sample_path = os.path.join(current_dir, "tests", "sample_code", "reverse_vowels_buggy.py")
        
# #         # Verify file exists
# #         if not os.path.exists(sample_path):
# #             raise FileNotFoundError(f"Test file missing: {sample_path}")
        
# #         with open(sample_path, 'r', encoding='utf-8') as f:
# #             code = f.read()
        
# #         # Ensure code is not empty
# #         if not code.strip():
# #             raise ValueError("Test file is empty")
        
# #         hints = self.generator.generate_hints("Reverse Vowels of a String", code)
# #         self.assertGreater(len(hints), 0)

# # if __name__ == "__main__":
# #     unittest.main()
# import os
# import sys
# import re
# import json
# import openai
# import unittest
# # Add project root to Python path
# project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.insert(0, project_root)

# from app.hint_system.code_analyzer import CodeAnalyzer

# class AdaptiveHintGenerator:
#     def __init__(self, questions_path, openai_api_key=None):
#         try:
#             with open(questions_path, 'r', encoding='utf-8') as f:
#                 self.questions = json.load(f)
#         except FileNotFoundError:
#             raise ValueError(f"Questions file not found at {questions_path}")
#         except json.JSONDecodeError:
#             raise ValueError("Invalid JSON format in questions file")
        
#         self.analyzers = {
#             q['question_name']: CodeAnalyzer() 
#             for q in self.questions
#         }
#         self.openai_api_key = openai_api_key
#         openai.api_key = openai_api_key
#         self.rules = self._load_rules()
    
#     def _load_rules(self):
#         from question_rules import QUESTION_HINT_RULES
#         return QUESTION_HINT_RULES
    
#     def generate_hints(self, question_name, user_code):
#         question = next(q for q in self.questions if q['question_name'] == question_name)
#         analyzer = self.analyzers[question_name]
        
#         # Static analysis
#         ast = analyzer.parse_ast(user_code)
#         if isinstance(ast, dict):
#             return [{"hint": f"Syntax Error: {ast['error']}", "type": "syntax"}]
        
#         issues = analyzer.find_issues(ast)
#         context = analyzer.analyze_problem_context(user_code)
        
#         # Collect all hints
#         hints = []
#         hints += self._apply_question_rules(question_name, user_code, issues)
#         hints += self._constraint_hints(question)
#         hints += [{"hint": issue, "type": "general"} for issue in issues]
        
#         # LLM Fallback if no meaningful hints
#         if len(hints) < 2 and self.openai_api_key:
#             llm_hint = self._generate_llm_hint(question, user_code, issues, context)
#             hints.append(llm_hint)
            
#         return hints[:3]

#     def _generate_llm_hint(self, question, user_code, issues, context):
#         try:
#             prompt = f"""Act as a coding tutor. Help fix this code for the problem:
#             {question['question']}
            
#             Constraints: {', '.join(question['constraints'])}
            
#             Student's Code:
#             {user_code}
            
#             Detected Issues: {', '.join(issues)}
#             Missing Concepts: {', '.join(context['missing_concepts'])}
            
#             Generate a helpful hint that:
#             1. Identifies one core misunderstanding
#             2. Suggests a solution approach without giving direct code
#             3. Asks a guiding question
#             Format: <strong>Issue</strong>: ... <strong>Approach</strong>: ... <strong>Question</strong>: ..."""
            
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You're a programming mentor providing helpful hints."},
#                     {"role": "user", "content": prompt}
#                 ],
#                 temperature=0.4,
#                 max_tokens=150
#             )
            
#             return {
#                 "hint": response.choices[0].message.content,
#                 "type": "llm",
#                 "confidence": 0.7
#             }
#         except Exception as e:
#             return {
#                 "hint": "Break the problem into smaller steps and test each part",
#                 "type": "fallback",
#                 "confidence": 0.5
#             }

#     def _apply_question_rules(self, question_name, code, issues):
#         hints = []
#         for rule in self.rules.get(question_name, []):
#             patterns = rule.get('patterns', [])
#             if any(re.search(p, code) for p in patterns):
#                 hints.extend({
#                     "hint": h,
#                     "type": "question-specific",
#                     "triggers": rule.get('trigger', 'unknown')
#                 } for h in rule.get('hints', []))
#         return hints
    
#     def _constraint_hints(self, question):
#         hints = []
#         constraints = "\n".join(question['constraints'])
        
#         if "O(1) space" in constraints:
#             hints.append({
#                 "hint": "Try to solve this with constant extra space",
#                 "type": "constraint"
#             })
#         if "without using division" in constraints:
#             hints.append({
#                 "hint": "Use prefix and suffix product arrays",
#                 "type": "constraint"
#             })
#         return hints

# class TestHintSystem(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         questions_path = os.path.join(current_dir, "questions.json")
#         cls.generator = AdaptiveHintGenerator(
#             questions_path,
#             openai_api_key=os.getenv("OPENAI_API_KEY")  # Set your API key here
#         )
    
#     def test_reverse_vowels(self):
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         sample_path = os.path.join(
#             current_dir, 
#             "tests", 
#             "sample_code", 
#             "reverse_vowels_buggy.py"
#         )
        
#         with open(sample_path, 'r', encoding='utf-8') as f:
#             code = f.read()
            
#         hints = self.generator.generate_hints(
#             "Reverse Vowels of a String", 
#             code
#         )
        
#         print("\nGenerated Hints:")
#         for h in hints:
#             print(f"- {h['hint']} ({h['type']})")
        
#         self.assertGreater(len(hints), 0)

# if __name__ == "__main__":
#     unittest.main()

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
    def __init__(self, questions_path, openai_api_key=None):
        with open(questions_path, 'r', encoding='utf-8') as f:
            self.questions = json.load(f)
        
        self.analyzers = {
            q['question_name']: CodeAnalyzer(problem_keywords=self._extract_keywords(q['question'])) 
            for q in self.questions
        }
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key
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
        hints += self._constraint_hints(question)
        hints += [{"hint": issue, "type": "general"} for issue in issues]

        if len(hints) > 2 and self.openai_api_key:
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
            cls.questions_path,
            openai_api_key="YOUR-API-KEY"
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
        questions_path,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)


# if __name__ == "__main__":
#     unittest.main()