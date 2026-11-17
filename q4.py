import numpy as np

# Generate 10,000 random numbers between 0 and 1
numbers = np.random.rand(10000)

# Calculate statistics
mean = np.mean(numbers)
minimum = np.min(numbers)
std_dev = np.std(numbers)

print("Mean:", mean)
print("Minimum:", minimum)
print("Standard Deviation:", std_dev)