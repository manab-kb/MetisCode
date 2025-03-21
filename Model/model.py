import numpy as np
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import tensorflow.keras.backend as K
from rlenv import MetisEnv

class A2C_Agent:
    def __init__(self, state_size, action_size, learning_rate=0.001):
        self.state_size = state_size
        self.action_size = action_size

        self.actor, self.critic = self.build_model()
        self.optimizer = Adam(learning_rate)

    def build_model(self):
        inputs = Input(shape=(self.state_size,))
        x = Dense(128, activation="relu")(inputs)
        x = Dense(64, activation="relu")(x)
        
        action_output = Dense(self.action_size, activation="sigmoid")(x)
        critic_output = Dense(1, activation="linear")(x)

        actor = Model(inputs, action_output)
        critic = Model(inputs, critic_output)

        return actor, critic

def compute_advantage(reward, value, gamma=0.99):
    return reward + gamma * value - value

def train_a2c(agent, env, episodes=1000, gamma=0.99):
    for episode in range(episodes):
        state = env.reset()
        episode_reward = 0

        for step in range(200):
            state = state.reshape(1, -1)
            action = agent.actor.predict(state)[0] * 10
            next_state, reward, done, _ = env.step(action)

            state_value = agent.critic.predict(state)[0]
            next_state_value = agent.critic.predict(next_state.reshape(1, -1))[0]
            advantage = compute_advantage(reward, state_value, gamma)

            agent.actor.fit(state, np.array([action]), verbose=0)
            agent.critic.fit(state, np.array([advantage]), verbose=0)

            state = next_state
            episode_reward += reward

            if done:
                break

        print(f"Episode {episode + 1}, Total Reward: {episode_reward:.2f}")

env = MetisEnv()
a2c_agent = A2C_Agent(state_size=7, action_size=1)
train_a2c(a2c_agent, env)
