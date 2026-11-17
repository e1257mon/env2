import numpy as np


numbers = np.random.rand(100)

mean = np.mean(numbers)
minimum = np.min(numbers)
std_dev = np.std(numbers)

print("Random Numbers:\n", numbers)
print("Mean:", mean)
print("Minimum:", minimum)
print("Standard Deviation:", std_dev)