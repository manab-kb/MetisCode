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
    "timestamp": "2025-04-02T12:34:56Z"
}

state = get_current_state(test_user_id)
print("Current state:", state)

success = update_question(test_user_id, test_question_id, test_question_data)
print("Question update successful:", success)
