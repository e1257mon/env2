
import numpy as np
import matplotlib.pyplot as plt

# 1. Total number of random points
N = 1000

# 2. Square area (9 x 9)
A = 9 * 9

# 3. Generate random points
np.random.seed(42)

x = np.random.uniform(0, 9, N)
y = np.random.uniform(0, 9, N)

# 4. Check whether points are inside the irregular figure
# Example irregular figure: Circle with center (4.5, 4.5) and radius 3

inside = (x - 4.5)**2 + (y - 4.5)**2 <= 9

# 5. Count points inside the irregular figure
M = np.sum(inside)

# 6. Calculate area
F = (M / N) * A

print("Total points (N):", N)
print("Points inside figure (M):", M)
print("Ratio (M/N):", M/N)
print("Estimated area:", F, "cm^2")

# Plot the points
plt.scatter(x[inside], y[inside], color='green', label='Inside')
plt.scatter(x[~inside], y[~inside], color='red', label='Outside')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Area Estimation")

plt.legend()
plt.show()