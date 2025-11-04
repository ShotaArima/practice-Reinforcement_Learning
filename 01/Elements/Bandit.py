import numpy as np

class Bandit:
    def __init__(self, arms=10):
        self.rates = np.random.randn(arms) # 一度設定したら変化しない

    def play(self, arm):
        rate = self.rates[arm]
        if rate > np.random.rand():
            return 1
        else :
            return 0