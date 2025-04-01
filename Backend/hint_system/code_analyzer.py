# import ast
# from zss import simple_distance, Node

# class CodeAnalyzer:
#     def __init__(self, correct_solution_ast=None):
#         self.correct_solution_ast = correct_solution_ast

#     def parse_ast(self, code):
#         try:
#             return ast.parse(code)
#         except SyntaxError as e:
#             return {"error": f"Syntax error: {e.msg} (line {e.lineno})"}
#         except Exception as e:
#             return {"error": str(e)}

#     def find_issues(self, ast_node):
#         issues = []
        
#         class Visitor(ast.NodeVisitor):
#             def __init__(self):
#                 self.issues = []
                
#             def visit_For(self, node):
#                 if isinstance(node.iter, ast.Call) and node.iter.func.id == 'range':
#                     self.issues.append("Potential off-by-one error in range()")
#                 self.generic_visit(node)
                
#         visitor = Visitor()
#         visitor.visit(ast_node)
#         return visitor.issues
import ast
from zss import simple_distance, Node

class CodeAnalyzer:
    def __init__(self, correct_solution_ast=None, problem_keywords=None):
        self.correct_solution_ast = correct_solution_ast
        self.problem_keywords = problem_keywords or []

    def parse_ast(self, code):
        """Parse code to AST with error handling"""
        try:
            return ast.parse(code)
        except SyntaxError as e:
            return {"error": f"Syntax error: {e.msg} (line {e.lineno})"}
        except Exception as e:
            return {"error": str(e)}

    def find_issues(self, ast_node):
        """Detect common code structure problems"""
        issues = []

        class Visitor(ast.NodeVisitor):
            def __init__(self):
                self.issues = []
                
            def visit_For(self, node):
                if isinstance(node.iter, ast.Call) and node.iter.func.id == 'range':
                    self.issues.append("Potential off-by-one error in range()")
                self.generic_visit(node)
                
            def visit_While(self, node):
                if isinstance(node.test, ast.Constant) and node.test.value:
                    self.issues.append("Potential infinite loop (while True)")
                self.generic_visit(node)

        visitor = Visitor()
        visitor.visit(ast_node)
        return visitor.issues

    def analyze_problem_context(self, user_code):
        """Check code alignment with problem requirements"""
        code_text = user_code.lower()
        if not self.problem_keywords:
            return {"keyword_coverage": 1.0, "missing_concepts": []}

        coverage = sum(
            keyword.lower() in code_text 
            for keyword in self.problem_keywords
        ) / len(self.problem_keywords)

        return {
            "keyword_coverage": coverage,
            "missing_concepts": [
                kw for kw in self.problem_keywords
                if kw.lower() not in code_text
            ]
        }

    def _compare_asts(self, ast_a, ast_b):
        """Compare AST similarity (optional)"""
        def build_zss_tree(node):
            if not node:
                return Node("")
            zss_node = Node(str(type(node).__name__))
            for child in ast.iter_child_nodes(node):
                zss_node.addkid(build_zss_tree(child))
            return zss_node

        return 1 - simple_distance(
            build_zss_tree(ast_a),
            build_zss_tree(ast_b)
        ) / 100