import numpy as np

class NonStatBandit:
    def __init__(self, arms=10):
        self.arms = arms
        self.rates = np.random.randn(arms) # 初期の成功確率

    def play(self, arm):
        rate = self.rates[arm]
        self.rates += np.random.randn(self.arms) * 0.1 # 毎回0.1のノイズを加える
        if rate > np.random.rand():
            return 1
        else :
            return 0
