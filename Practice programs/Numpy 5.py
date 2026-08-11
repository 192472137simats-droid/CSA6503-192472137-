import numpy as np

np.random.seed(42)
data = np.random.randint(1, 100, 10)
print("Data:", data)
print("Std Dev:", np.std(data))
print("Median:", np.median(data))
print("Sorted:", np.sort(data))
