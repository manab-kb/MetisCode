import requests
import json

BASE_URL = "http://localhost:5001"

def test_testcase():
    url = f"{BASE_URL}/testcases"
    payload = {
        "question_name": "String Compression"
    }
    response = requests.post(url, json=payload)
    print("=== /testcase Endpoint ===")
    print("Status Code:", response.status_code)
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        print("Response Text:", response.text)
    print()

def test_current_state():
    user_id = "user123"  # 请根据实际情况修改 user_id
    url = f"{BASE_URL}/state/current/{user_id}"
    response = requests.get(url)
    print("=== /state/current Endpoint ===")
    print("URL:", url)
    print("Status Code:", response.status_code)
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        print("Response Text:", response.text)
    print()

def test_question_state_get():
    user_id = "user123"         # 根据实际情况修改
    question_id = "StringCompression"  # 根据实际情况修改
    url = f"{BASE_URL}/state/question/{user_id}/{question_id}"
    response = requests.get(url)
    print("=== /state/question (GET) Endpoint ===")
    print("URL:", url)
    print("Status Code:", response.status_code)
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        print("Response Text:", response.text)
    print()

def test_question_state_update():
    user_id = "user123"         # 根据实际情况修改
    question_id = "StringCompression"  # 根据实际情况修改
    url = f"{BASE_URL}/state/question/{user_id}/{question_id}"
    payload = {
        "time_taken": 30.0,
        "test_cases_passed": 5.0,
        "attempts": 2.0,
        "hints_used": 1.0,
        "difficulty_level": 3.0,
        "fatigue": 0.5,
        "streak_bonus": 1.0
    }
    response = requests.post(url, json=payload)
    print("=== /state/question (POST update) Endpoint ===")
    print("URL:", url)
    print("Status Code:", response.status_code)
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data, indent=4))
    except json.JSONDecodeError:
        print("Response Text:", response.text)
    print()

if __name__ == "__main__":
    print("Starting API tests...\n")
    
    test_testcase()
    
    test_current_state()
    
    test_question_state_get()
    
    test_question_state_update()
    
    test_question_state_get()
    
    print("API tests completed.")
