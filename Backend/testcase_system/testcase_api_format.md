### problems Testcase API Format
URL: http://localhost:5001/testcase  
Method: POST  
Header 'Content-Type: application/json'  
Data
```
{
    "question_name": "String Compression"  
}
```

Status Code: 200  
Response JSON:
```
[
    {
        "input": {
            "chars": [
                "a",
                "a",
                "b",
                "b",
                "c",
                "c",
                "c"
            ]
        },
        "output": "6"
    },
    {
        "input": {
            "chars": [
                "a"
            ]
        },
        "output": "1"
    },
    {
        "input": {
            "chars": [
                "a",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b",
                "b"
            ]
        },
        "output": "4"
    }
]
```  

### get current user state API Format
URL: http://localhost:5001/state/current/<user_id>  
(http://localhost:5001/state/current/user123)  
Method: GET  
Header 'Content-Type: application/json'  

Status Code: 200  
Response JSON:
```
{
    "attempts": 2.0,
    "difficulty_level": 3.0,
    "fatigue": 0.5,
    "hints_used": 1.0,
    "streak_bonus": 1.0,
    "test_cases_passed": 5.0,
    "time_taken": 30.0,
    "timestamp": "2025-04-06T22:59:36.366465"
}
```

### get user history problem of progress API Format
URL: http://localhost:5001/state/question/get/<user_id>/<question_id>  
(http://localhost:5001/state/question/user123/StringCompression)  
Method: GET  
Header 'Content-Type: application/json'  

Status Code: 200  
Response JSON:
```
{
    "attempts": 2.0,
    "difficulty_level": 3.0,
    "fatigue": 0.5,
    "hints_used": 1.0,
    "streak_bonus": 1.0,
    "test_cases_passed": 5.0,
    "time_taken": 30.0,
    "timestamp": "2025-04-06T22:59:36.366465"
}
```

### update user model API Format
URL: http://localhost:5001/state/question/update/<user_id>/<question_id>  
(http://localhost:5001/state/question/update/user123/StringCompression)  
Data
```
{
    "time_taken": 30.0,
    "test_cases_passed": 5.0,
    "attempts": 2.0,
    "hints_used": 1.0,
    "difficulty_level": 3.0,
    "fatigue": 0.5,
    "streak_bonus": 1.0,
    "timestamp"(optional, if there is no time, will default use the current time):  
        "2025-04-06T23:09:51.926827"
}
```

Response JSON:
```
{
    "attempts": 2.0,
    "difficulty_level": 3.0,
    "fatigue": 0.5,
    "hints_used": 1.0,
    "streak_bonus": 1.0,
    "test_cases_passed": 5.0,
    "time_taken": 30.0,
    "timestamp": "2025-04-06T23:09:51.926827"
}
```