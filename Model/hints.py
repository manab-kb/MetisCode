from transformers import pipeline

hint_model = pipeline("text-generation", model="Salesforce/codet5-small")

# TODO: Change hints based on solution dataset
def generate_hint(problem_statement, incorrect_code):
    prompt = f"Problem: {problem_statement}\nIncorrect Code: {incorrect_code}\nHint:"
    hint = hint_model(prompt, max_length=100)
    return hint[0]["generated_text"]
