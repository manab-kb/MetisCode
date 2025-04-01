import os
import json

def parse_question_file(file_path):
    """Extracts question, examples, and constraints from a `_Q.py` file."""
    question_name = os.path.basename(file_path).replace("_Q.py", "")  # Extract question name
    question_data = {
        "question_name": question_name,
        "question": "",
        "examples": [],
        "constraints": [],
        "difficulty": ""
    }
    
    print(f"📂 Reading file: {file_path}")  # Debugging

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return None  # Skip file if error occurs

    if not lines:
        print(f"⚠️ Warning: {file_path} is empty!")
        return None  # Skip empty files

    section = "question"
    example_buffer = []

    for line in lines:
        stripped_line = line.strip()

        if not stripped_line:
            continue  # Skip empty lines

        if stripped_line.startswith("Example"):
            section = "examples"
            if example_buffer:
                question_data["examples"].append("\n".join(example_buffer))
                example_buffer = []
            continue
        
        if stripped_line.startswith("Constraints:"):
            section = "constraints"
            if example_buffer:
                question_data["examples"].append("\n".join(example_buffer))
                example_buffer = []
            continue
        
        if section == "question":
            question_data["question"] += stripped_line + " "
        elif section == "examples":
            example_buffer.append(stripped_line)
        elif section == "constraints":
            question_data["constraints"].append(stripped_line)
    
    if example_buffer:
        question_data["examples"].append("\n".join(example_buffer))
    
    difficulty = 0
    question_data["difficulty"] = difficulty

    print(f"✅ Parsed: {question_name}")  # Debugging
    return question_data

def find_question_files(directory):
    """Find and parse '_Q.py' files, categorizing them by structure."""
    question_list = []

    print(f"🔍 Scanning directory: {directory}")  # Debugging

    for root, dirs, files in os.walk(directory):
        print(f"📂 Checking folder: {root}")  # Debugging

        for file in files:
            if file.endswith("_Q.py"):  # FIX: Now looking for `_Q.py`
                file_path = os.path.join(root, file)
                print(f"📄 Found question file: {file_path}")  # Debugging
                
                question_data = parse_question_file(file_path)

                if question_data:
                    question_list.append(question_data)

    return question_list

def display_questions(questions):
    """Display the first 5 and last 5 questions and show total count."""
    num_questions = len(questions)
    if num_questions == 0:
        print("❌ No questions found.")
        return
    
    print("\n📌 First 5 Questions:")
    for q in questions[:5]:
        print(f"\n🔹 Question: {q['question_name']}")
        print(f"❓ {q['question']}")
        if q["examples"]:
            print("📝 Example:")
            for ex in q["examples"]:
                print(f"   {ex}")
        if q["constraints"]:
            print("⚙️ Constraints:")
            for c in q["constraints"]:
                print(f"   {c}")

    if num_questions > 5:
        print("\n📌 Last 5 Questions:")
        for q in questions[-5:]:
            print(f"\n🔹 Question: {q['question_name']}")
            print(f"❓ {q['question']}")
            if q["examples"]:
                print("📝 Example:")
                for ex in q["examples"]:
                    print(f"   {ex}")
            if q["constraints"]:
                print("⚙️ Constraints:")
                for c in q["constraints"]:
                    print(f"   {c}")
    
    # Display total number of questions found
    print(f"\n✅ Total Questions Extracted: {num_questions}")

def save_questions_to_json(questions, filename="questions.json"):
    """Save extracted questions to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(questions, json_file, indent=4, ensure_ascii=False)
        print(f"\n💾 Questions saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving JSON file: {e}")

def main():
    directory = input("Enter the directory path: ").strip()
    if not os.path.isdir(directory):
        print("❌ Invalid directory. Please enter a valid path.")
        return
    
    question_list = find_question_files(directory)
    display_questions(question_list)
    save_questions_to_json(question_list)  # Save to JSON file

if __name__ == "__main__":
    main()
