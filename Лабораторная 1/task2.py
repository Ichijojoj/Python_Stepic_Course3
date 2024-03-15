import numpy as np

# Создаем пустую матрицу размером 5x9
matrix = np.zeros((9, 9), dtype=int)

# Заполняем матрицу построчно
for i in range(9):
    for j in range(9):
        if (i + j) % 2 == 0:
            matrix[i][j] = 1

print(matrix)
