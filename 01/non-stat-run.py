import matplotlib.pyplot as plt
import numpy as np

from Elements.Agent import Agent
from Elements.Bandit import Bandit
from Elements.AlphaAgent import AlphaAgent
from Elements.NonStatBandit import NonStatBandit

runs = 200
steps = 1000
epsilon = 0.1
alpha = 0.8

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

stat_avg_rates = np.average(all_rates, axis=0)



all_rates = np.zeros((runs, steps)) #(200, 1000)の形状の配列に初期化

for run in range(runs):
    bandit = NonStatBandit()
    agent = AlphaAgent(epsilon, alpha)
    total_reward = 0
    rates = []

    for step in range(steps):
        action = agent.get_action()
        reward = bandit.play(action)
        agent.update(action, reward)
        total_reward += reward
        rates.append(total_reward / (step+1))

    all_rates[run] = rates

non_stat_avg_rates = np.average(all_rates, axis=0)


# グラフの描画
plt.figure()
plt.plot(stat_avg_rates, label="Statinary")
plt.plot(non_stat_avg_rates, label="Non-Statinary")
plt.xlabel("Steps")
plt.ylabel("Rates")
plt.title("AVG-Rates over Time")
plt.legend()
plt.savefig("outputs/avg-rates(stat vs nonstat).png")