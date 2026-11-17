
import numpy as np
import matplotlib.pyplot as plt

# 1. Number of epochs
N = 50

# 2. Initial position
x = 0
y = 0
z = 0

# Store positions
X = [x]
Y = [y]
Z = [z]

# 3. Movement probabilities
directions = ['L', 'R', 'F', 'B']
probabilities = [0.25, 0.35, 0.30, 0.10]

vertical = ['U', 'D']
vertical_prob = [0.80, 0.20]

# 4. Simulation
np.random.seed(42)

for i in range(N):

    # Horizontal movement
    move = np.random.choice(directions, p=probabilities)

    if move == 'L':
        x -= 1
    elif move == 'R':
        x += 1
    elif move == 'F':
        y += 1
    else:
        y -= 1

    # Vertical movement
    up_down = np.random.choice(vertical, p=vertical_prob)

    if up_down == 'U':
        z += 1
    else:
        z -= 1

    # Store position
    X.append(x)
    Y.append(y)
    Z.append(z)

# 5. Final location
print("Final X position:", x)
print("Final Y position:", y)
print("Final Z position:", z)

print("Final Location:", (x, y, z))

# 6. Plot the movement
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(X, Y, Z, marker='o', markersize=3)

ax.set_xlabel("X - Left/Right")
ax.set_ylabel("Y - Forward/Backward")
ax.set_zlabel("Z - Up/Down")

ax.set_title("Flying Object Movement")

plt.show()
