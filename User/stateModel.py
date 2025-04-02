# stateModel.py
from datetime import datetime
from typing import Optional
import numpy as np

class StateModel:
    def __init__(self, time_taken: float = 0.0, test_cases_passed: float = 0.0, attempts: float = 0.0,
                 hints_used: float = 0.0, difficulty_level: float = 0.0, fatigue: float = 0.0, 
                 streak_bonus: float = 0.0, timestamp: Optional[datetime] = None):
        self.time_taken = time_taken
        self.test_cases_passed = test_cases_passed
        self.attempts = attempts
        self.hints_used = hints_used
        self.difficulty_level = difficulty_level
        self.fatigue = fatigue
        self.streak_bonus = streak_bonus
        self.timestamp = timestamp if timestamp is not None else datetime.now()

    @classmethod
    def from_dict(cls, data: dict):
        timestamp = data.get("timestamp")
        if timestamp is not None:
            timestamp = datetime.fromisoformat(timestamp)
        return cls(
            time_taken=data.get("time_taken", 0.0),
            test_cases_passed=data.get("test_cases_passed", 0.0),
            attempts=data.get("attempts", 0.0),
            hints_used=data.get("hints_used", 0.0),
            difficulty_level=data.get("difficulty_level", 0.0),
            fatigue=data.get("fatigue", 0.0),
            streak_bonus=data.get("streak_bonus", 0.0),
            timestamp=timestamp
        )

    def to_list(self):
        return [self.time_taken, self.test_cases_passed, self.attempts,
                self.hints_used, self.difficulty_level, self.fatigue, self.streak_bonus]

    def to_numpy(self):
        return np.array(self.to_list(), dtype=np.float32)

    def to_dict(self):
        return {
            "time_taken": self.time_taken,
            "test_cases_passed": self.test_cases_passed,
            "attempts": self.attempts,
            "hints_used": self.hints_used,
            "difficulty_level": self.difficulty_level,
            "fatigue": self.fatigue,
            "streak_bonus": self.streak_bonus,
            "timestamp": self.timestamp.isoformat()
        }

    def __str__(self):
        return f"InputState({self.to_list()})"
