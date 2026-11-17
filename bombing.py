
import numpy as np
import matplotlib.pyplot as plt

# 1. Simulation settings
sorties = 50
bombs = 10
N = sorties * bombs

# 2. Generate normal random numbers
np.random.seed(42)

zx = np.random.normal(0, 1, N)
zy = np.random.normal(0, 1, N)

# 3. Calculate bomb strike coordinates
x = 500 * zx
y = 300 * zy

# 4. Check hit or miss
hit = (abs(x) <= 500) & (abs(y) <= 300)

# 5. Count hits and misses
total_hits = np.sum(hit)
total_misses = N - total_hits

# 6. Calculate hit percentage
percentage = (total_hits / N) * 100

print("Total Bombs:", N)
print("Number of Hits:", total_hits)
print("Number of Misses:", total_misses)
print("Percentage of Hits:", percentage, "%")

# 7. Plot the bomb strikes

# Plot
plt.scatter(x[hit], y[hit], color='green', label='Hit')
plt.scatter(x[~hit], y[~hit], color='red', label='Miss')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bombing Simulation")

plt.legend()
plt.grid()
plt.show()

