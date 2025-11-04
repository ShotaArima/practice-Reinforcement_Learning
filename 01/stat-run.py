import matplotlib.pyplot as plt

from Elements.Agent import Agent
from Elements.Bandit import Bandit

steps = 1000
epsilon = 0.1

bandit = Bandit()
agent = Agent(epsilon)
total_reward = 0
total_rewards = []
rates = []

for step in range(steps):
    action = agent.get_action()
    reward = bandit.play(action)
    agent.update(action, reward)
    total_reward += reward

    total_rewards.append(total_reward)
    rates.append(total_reward / (step+1))

print(total_rewards)

# グラフの描画
plt.figure()
plt.plot(total_rewards)
plt.xlabel("Steps")
plt.ylabel("Total Reward")
plt.title("Total Reward over Time")
plt.savefig("outputs/total_reward.png")

# グラフの描画
plt.figure()
plt.plot(rates)
plt.xlabel("Steps")
plt.ylabel("Rates")
plt.title("Rates over Time")
plt.savefig("outputs/rates.png")