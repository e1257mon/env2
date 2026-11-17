
import numpy as np


N = 1000

# Store results
total_trials = []
total_cost = []

for i in range(N):

    H = 0
    T = 0
    trials = 0

    while abs(H - T) < 20:

        # Roll a six-sided dice
        dice = np.random.randint(1, 7)

        # Odd = H, Even = T
        if dice % 2 == 1:
            H += 1
        else:
            T += 1

        trials += 1

    # Each trial costs $1
    cost = trials * 1

    total_trials.append(trials)
    total_cost.append(cost)

# Calculate average
print("Average Trials:", np.mean(total_trials))
print("Average Cost: $", np.mean(total_cost))

print("Minimum Cost: $", min(total_cost))
print("Maximum Cost: $", max(total_cost))

# Plot histogram
import matplotlib.pyplot as plt

plt.hist(total_trials, bins=20, edgecolor='black')

plt.xlabel("Number of Trials")
plt.ylabel("Frequency")
plt.title("Monte Carlo Gambling Game")

plt.show()
