import numpy as np
from typing import List, Tuple

class RLAgent:
    def __init__(self, num_states: int, num_actions: int, alpha: float, gamma: float, epsilon: float):
        self.Q = np.zeros((num_states, num_actions))
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_actions = num_actions
    
    def choose_action(self, state: int) -> int:
        if np.random.uniform() < self.epsilon:
            action = np.random.choice(self.num_actions)
        else:
            values = self.Q[state, :]
            action = np.random.choice([a for a, v in enumerate(values) if v == np.max(values)])
        return action
    
    def learn(self, state: int, action: int, reward: float, next_state: int, done: bool):
        current_value = self.Q[state, action]
        next_max = np.max(self.Q[next_state, :])
        td_target = reward + self.gamma * next_max * (1.0 - done)
        new_value = current_value + self.alpha * (td_target - current_value)
        self.Q[state, action] = new_value
