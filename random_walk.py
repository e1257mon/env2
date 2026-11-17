
import numpy as np
import matplotlib.pyplot as plt

# 1. Number of steps
n = 50

# 2. Generate random numbers
np.random.seed(42)
random_numbers = np.random.randint(0, 10, n)

# 3. Starting position
x = 0
y = 0

# Store positions
x_positions = [x]
y_positions = [y]

# 4. Random walk simulation
for r in random_numbers:

    if r <= 3:
        # Forward
        y = y + 1

    elif r <= 5:
        # Backward
        y = y - 1

    elif r <= 7:
        # Left
        x = x - 1

    else:
        # Right
        x = x + 1

    x_positions.append(x)
    y_positions.append(y)

# 5. Final position
print("Final Position:", (x, y))

# 6. Plot
plt.plot(x_positions, y_positions, marker='o')

plt.scatter(0, 0, color='green', label='Start')
plt.scatter(x, y, color='red', label='End')

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Random Walk Simulation")
plt.legend()
plt.grid()
plt.show()
