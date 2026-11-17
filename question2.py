
import numpy as np
import matplotlib.pyplot as plt

# 1. Number of customers
n = 1000

# 2. Generate inter-arrival times
inter_arrival = np.random.exponential(scale=5, size=n)

# 3. Generate service times
service_time = np.random.uniform(low=2, high=8, size=n)

# 4. Calculate sample statistics

# Inter-arrival statistics
ia_mean = np.mean(inter_arrival)
ia_std = np.std(inter_arrival, ddof=1)

# Service time statistics
st_mean = np.mean(service_time)
st_std = np.std(service_time, ddof=1)

# 5. Plot histograms
plt.subplot(1, 2, 1)
plt.hist(inter_arrival, bins=30)
plt.title("Inter-arrival Time")
plt.xlabel("Time")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(service_time, bins=30)
plt.title("Service Time")
plt.xlabel("Time")
plt.ylabel("Frequency")

plt.show()

# 6. Theoretical statistics

# Exponential distribution
theoretical_ia_mean = 5
theoretical_ia_std = 5

# Uniform distribution
theoretical_st_mean = (2 + 8) / 2
theoretical_st_std = (8 - 2) / np.sqrt(12)

# 7. Display comparison
print("INTER-ARRIVAL TIME")
print("Sample Mean:", ia_mean)
print("Theoretical Mean:", theoretical_ia_mean)
print("Sample Std:", ia_std)
print("Theoretical Std:", theoretical_ia_std)

print("\nSERVICE TIME")
print("Sample Mean:", st_mean)
print("Theoretical Mean:", theoretical_st_mean)
print("Sample Std:", st_std)
print("Theoretical Std:", theoretical_st_std)
