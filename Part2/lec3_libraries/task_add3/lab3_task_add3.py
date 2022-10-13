import numpy as np

print("Введите значения размерности массива(число строк и столбцов) через пробел:");
rows, columns = map(int, input().split())
print("Введите значения элементов массива через пробел:");
values = list(map(int, input().split()));
mas = np.array(values).reshape(rows, columns)
print(mas)
print(np.amax(mas, axis=0))
