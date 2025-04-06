from flask import Flask, request, jsonify
import json

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from User.dataApi import get_current_state, get_question_state, update_question

app = Flask(__name__)

with open('./Backend/testcase_system/all_testcases.json', 'r', encoding='utf-8') as f:
    all_testcases = json.load(f)

@app.route('/testcases', methods=['POST'])
def get_testcases():
    data = request.get_json()
    if not data or "question_name" not in data:
        return jsonify({"error": "The request must include the 'question_name' field"}), 400

    question_name = data.get("question_name")
    
    for testcase in all_testcases:
        if testcase.get("question_name") == question_name:
            return jsonify(testcase.get("test_cases"))
    
    return jsonify({"error": "Question not found"}), 500

@app.route('/state/current/<user_id>', methods=['GET'])
def current_state(user_id):
    state = get_current_state(user_id)
    if state is not None:
        return jsonify(state.to_dict())
    else:
        return jsonify({"error": "Current state not found for user"}), 404

@app.route('/state/question/<user_id>/<question_id>', methods=['GET'])
def question_state(user_id, question_id):
    state = get_question_state(user_id, question_id)
    if state is not None:
        return jsonify(state.to_dict())
    else:
        return jsonify({"error": "State not found for the specified question and user"}), 404

@app.route('/state/question/<user_id>/<question_id>', methods=['POST'])
def update_question_state(user_id, question_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided for update"}), 400

    # Create a StateModel instance from the provided dictionary.
    try:
        from User.stateModel import StateModel
        state_data = StateModel.from_dict(data)
    except Exception as e:
        return jsonify({"error": f"Invalid state data: {e}"}), 400

    success = update_question(user_id, question_id, state_data)
    if success:
        return jsonify({"message": "State updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update state"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
