import numpy as np

class AlphaAgent:
    def __init__(self, epsilon, alpha, actions=10):
        self.epsilon = epsilon
        self.Qs = np.zeros(actions)
        self.alpha = alpha

    def update(self, action, reward):
        self.Qs[action] += self.alpha * (reward - self.Qs[action])

    def get_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(len(self.Qs))
        else:
            return np.argmax(self.Qs)