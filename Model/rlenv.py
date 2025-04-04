import gym
import json
import numpy as np
from gym import spaces

class MetisEnv(gym.Env):
    def __init__(self, json_path="../Data/Leetcode/questions.json"):
        super(MetisEnv, self).__init__()

        with open(json_path, 'r') as f:
            self.dataset = json.load(f)

        self.index = 0 
        self.total_data = len(self.dataset)

        self.observation_space = spaces.Box(low=0, high=1, shape=(7,), dtype=np.float32)
        self.action_space = spaces.Box(low=0, high=10, shape=(1,), dtype=np.float32)

        self.state = self._get_state(self.dataset[self.index])

    def _get_state(self, entry):
        time_taken = entry["time_taken"]
        test_cases_passed = entry["test_cases_passed"]
        attempts = entry["attempts"]
        hints_used = entry["hints_used"]
        difficulty_level = entry["difficulty"]

        fatigue = abs(attempts / (difficulty_level + 0.1))
        streak_bonus = 1 if test_cases_passed >= 8 else -1

        state = np.array([
            time_taken / 300,
            test_cases_passed / 10,
            attempts / 10,
            hints_used / 5,
            difficulty_level / 10,
            fatigue,
            streak_bonus
        ], dtype=np.float32)

        return state

    def step(self, action):
        entry = self.dataset[self.index]
        difficulty_level = np.clip(action[0], 0, 10)

        reward = (
            entry["test_cases_passed"]
            - (0.05 * entry["time_taken"])
            - (0.2 * entry["attempts"])
            - (0.3 * entry["hints_used"])
            - (0.4 * abs(entry["attempts"] / (difficulty_level + 0.1)))
        )

        self.index = (self.index + 1) % self.total_data
        self.state = self._get_state(self.dataset[self.index])
        done = self.index == self.total_data - 1
        return self.state, reward, done, {}

    def reset(self):
        self.index = 0
        self.state = self._get_state(self.dataset[self.index])
        return self.state
