
import numpy as np
import matplotlib.pyplot as plt

# 1. Number of random points
N = 100000

# 2. Generate random points
np.random.seed(42)

x = np.random.uniform(0, 1, N)
y = np.random.uniform(0, 1, N)

# 3. Check points inside the circle
inside = (x**2 + y**2) <= 1

# 4. Different sample sizes
sample_sizes = [100, 1000, 10000, 100000]

pi_estimates = []

# 5. Calculate Pi for each sample size
for n in sample_sizes:

    inside_count = 0

    for i in range(n):
        if inside[i] == True:
            inside_count += 1

    # Calculate estimated Pi
    pi_estimate = 4 * inside_count / n

    pi_estimates.append(pi_estimate)

    print("Number of points:", n)
    print("Inside points:", inside_count)
    print("Estimated Pi:", pi_estimate)
    print()

# 6. Plot the graph
plt.plot(sample_sizes, pi_estimates, 'o-')

plt.axhline(np.pi, color='red', linestyle='--')

plt.xlabel("Number of Points")
plt.ylabel("Estimated Pi")
plt.title("Monte Carlo Estimation of Pi")

plt.grid()
plt.show()
