import numpy as np
rows = int(input("Введите число строк в матрицах:"));
columns = int(input("Введите число столбцов в матрицах:"));

print(f"Введите значения {rows * columns} элементов первой матрицы через пробел:");
values1 = list(map(int, input().split()));

if len(values1) != rows * columns:
  while len(values1) < rows * columns:
    values1.append(0);
  while len(values1) > rows * columns:
    values1.remove[values1[-1]];

print(f"Введите значения {rows * columns} элементов второй матрицы через пробел:");
values2 = list(map(int, input().split()));

if len(values2) != rows * columns:
  while len(values2) < rows * columns:
    values2.append(0);
  while len(values2) > rows * columns:
    values2.remove(values2[-1]);

mas1 = np.array(values1).reshape(rows, columns);
mas2 = np.array(values2).reshape(rows, columns);
print(mas1);
print(mas2);

valuesfin = [0 for i in range(rows * columns)]
mas3 = np.array(valuesfin).reshape(rows, columns);
for i in range(0, rows):
  for j in range(0, columns):
    mas3[i][j] = np.maximum(mas1[i][j], mas2[i][j]);
print(mas3);