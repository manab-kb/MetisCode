import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from User.dataApi import *

# Replace with valid test values
test_user_id = "user_id_123"
test_question_id = "question_456"
test_question_data = {
    "time_taken": 0.5,
    "test_cases_passed": 0.9,
    "attempts": 0.2,
    "hints_used": 0.1,
    "difficulty_level": 0.8,
    "fatigue": 0.4,
    "streak_bonus": 1.0,
}

state = get_current_state(test_user_id)
print("Current state:", state)

state_obj = StateModel.from_dict(test_question_data)

success = update_question(test_user_id, test_question_id, state_obj)
print("Question update successful:", success)
