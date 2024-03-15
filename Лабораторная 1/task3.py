import numpy as np

np.random.seed(42)
vector = np.random.random(10)
array = np.array([])
array = vector
sorted_array = np.sort(array)

print("Отсортированный массив:", sorted_array)