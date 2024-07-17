import numpy as np

array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique, counts = np.unique(array, return_counts=True)
frequency = dict(zip(unique, counts))
print("Frequency of unique values:", frequency)
