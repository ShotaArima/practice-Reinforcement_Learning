import matplotlib.pyplot as plt
import numpy as np

from Elements.Agent import Agent
from Elements.Bandit import Bandit

runs = 200
steps = 1000
epsilon = 0.1
all_rates = np.zeros((runs, steps)) #(200, 1000)の形状の配列

for run in range(runs):
    bandit = Bandit()
    agent = Agent(epsilon)
    total_reward = 0
    rates = []

    for step in range(steps):
        action = agent.get_action()
        reward = bandit.play(action)
        agent.update(action, reward)
        total_reward += reward
        rates.append(total_reward / (step+1))

    all_rates[run] = rates

avg_rates = np.average(all_rates, axis=0)

# グラフの描画
plt.figure()
plt.plot(avg_rates)
plt.xlabel("Steps")
plt.ylabel("Rates")
plt.title("AVG-Rates over Time")
plt.savefig("outputs/avg-rates.png")