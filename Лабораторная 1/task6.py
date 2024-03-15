import numpy as np

array = np.zeros((2, 3, 2))
linear_index = 9
index = np.unravel_index(linear_index, array.shape)

print("Индекс 9 элемента:", index)