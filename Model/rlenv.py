import gym
import numpy as np
from gym import spaces
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Flatten

class MetisEnv(gym.Env):
    def __init__(self):
        super(MetisEnv, self).__init__()

        self.observation_space = spaces.Box(low=0, high=1, shape=(7,), dtype=np.float32)
        self.action_space = spaces.Box(low=0, high=10, shape=(1,), dtype=np.float32)
        self.state = np.random.rand(7)

    def step(self, action):
        difficulty_level = np.clip(action[0], 0, 10)

        time_taken = np.random.uniform(10, 300) / (difficulty_level + 1) # Temporarily Removed due to Dataset
        test_cases_passed = np.random.randint(1, 10) if difficulty_level < 7 else np.random.randint(0, 10)
        attempts = np.random.randint(1, 5) if difficulty_level < 7 else np.random.randint(2, 8)
        hints_used = np.random.randint(0, 3)
        fatigue = np.abs(self.state[5] - (attempts / difficulty_level))
        streak_bonus = 1 if test_cases_passed > 7 else -1

        self.state = np.array([
            time_taken / 300,
            test_cases_passed / 10,
            attempts / 10,
            hints_used / 5,
            difficulty_level / 10,
            fatigue,
            streak_bonus
        ], dtype=np.float32)

        reward = test_cases_passed - (0.05 * time_taken) - (0.2 * attempts) - (0.3 * hints_used) - (0.4 * fatigue)
        
        done = False
        return self.state, reward, done, {}

    def reset(self):
        self.state = np.random.rand(7)
        return self.state
