import numpy as np
rows  = 5
columns = 5
print("Введите значения 24 элементов матрицы через пробел:");
values = list(map(int, input().split()));

if len(values) != 24:
  while len(values) < 24:
    values.append(0);
  while len(values) > 24:
    values.remove(values[-1]);
values.append(0);
mas = np.array(values).reshape(5, 5);
print(mas);

num = int(input("Введите значение элемента, который необходимо вставить:"));
print("Введите номера строки и столбца, в которые нужно вставить элемент:")
row, column = map(int, input().split())
values.insert(((row - 1) * columns + column - 1),num);
values.remove(values[-1]);
mas = np.array(values).reshape(5, 5);
print(mas)