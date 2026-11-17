import numpy as np

np.random.seed(42)
numbers1 = np.random.rand(100)

np.random.seed(42)
numbers2 = np.random.rand(100)

print("First Mean:", np.mean(numbers1))
print("Second Mean:", np.mean(numbers2))

print("First Minimum:", np.min(numbers1))
print("Second Minimum:", np.min(numbers2))

print("First Standard Deviation:", np.std(numbers1))
print("Second Standard Deviation:", np.std(numbers2))


print("Are arrays identical?", np.array_equal(numbers1, numbers2))