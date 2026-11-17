
import numpy as np

# 1. Number of games
n = 10000

# 2. Game settings
total_cost = 0
total_reward = 0
total_flips = 0

# 3. Simulate games
for game in range(n):

    head = 0
    tail = 0
    flips = 0

    while abs(head - tail) != 3:

        # Generate random number (0 to 9)
        r = np.random.randint(0, 10)

        # Check Head or Tail
        if r <= 4:
            head = head + 1
        else:
            tail = tail + 1

        flips = flips + 1

    # Calculate cost and reward
    total_cost = total_cost + flips
    total_reward = total_reward + 8
    total_flips = total_flips + flips

# 4. Calculate results
average_flips = total_flips / n
total_profit = total_reward - total_cost
average_profit = total_profit / n

# 5. Display results
print("Total Games:", n)
print("Average Flips:", average_flips)
print("Total Cost:", total_cost)
print("Total Reward:", total_reward)
print("Total Profit:", total_profit)
print("Average Profit per Game:", average_profit)

if average_profit > 0:
    print("You will WIN in the long run.")
elif average_profit < 0:
    print("You will LOSE in the long run.")
else:
    print("No Profit, No Loss.")
