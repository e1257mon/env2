
import numpy as np
import matplotlib.pyplot as plt

# 1. Number of random points
N = 10000

# 2. Rectangle area
a = 2
b = 5
H = 140

A = (b - a) * H

# 3. Generate random points
np.random.seed(42)

x = np.random.uniform(a, b, N)
y = np.random.uniform(0, H, N)

# 4. Check points below the curve y = x^3
inside = y <= x**3

# 5. Count points below the curve
M = np.sum(inside)

# 6. Calculate integral
I = (M / N) * A

print("Total points (N):", N)
print("Points below curve (M):", M)
print("Estimated Integral:", I)

# 7. Actual integral
actual = (5**4 - 2**4) / 4

print("Actual Integral:", actual)

# 8. Plot
plt.scatter(x[inside], y[inside], color='green', s=3)
plt.scatter(x[~inside], y[~inside], color='red', s=3)

# Draw the curve
X = np.linspace(2, 5, 100)
plt.plot(X, X**3, color='blue')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Monte Carlo Numerical Integration")

plt.show()
