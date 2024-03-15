import numpy as np

np.random.seed(42)
fourth_array = np.random.randint(3, 5,(8, 3))
rows_with_all_fours = np.all(fourth_array == 4, axis=1)

if np.any(rows_with_all_fours):
    print("Есть строки, где все значения равны 4")
    # получение индексов строк, в которых все значения равны 4:
    print("Индексы таких строк:", np.where(rows_with_all_fours)[0])
else:
    print("Нет строк, где все значения равны 4")