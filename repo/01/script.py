import numpy as np
import matplotlib.pyplot as plt
from src.bandit import Bandit
from src.Agent import Agent

runs = 200
steps = 10000
epsilon = [0.01, 0.1, 0.3]
all_rates = np.zeros((runs, steps))

for e in epsilon:
    for run in range(runs):
        bandit = Bandit()
        agent = Agent(e)
        total_reward = 0
        rates = []

        for step in range(steps):
            action = agent.get_action()
            reward = bandit.play(action)
            agent.update(action, reward)
            total_reward += reward
            rates.append(total_reward / (step + 1))

        all_rates[run] = rates

    avg_rates = np.average(all_rates, axis=0)

    # plt.figure()
    # plt.ylim(bottom=0)
    plt.ylabel("Rates")
    plt.xlabel("Steps")
    plt.plot(avg_rates)
    plt.savefig(f"/repo/01/outputs/rates.png")
