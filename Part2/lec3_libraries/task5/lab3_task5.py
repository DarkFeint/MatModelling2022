import numpy as np

def mas(rows, columns, col1, col2):
  mas = np.zeros((rows, columns));
  colmin = np.minimum(col1, col2);
  colmax = np.maximum(col1, col2);
  for i in range(0, rows):
    for j in range(0, columns):
      mas[i][j] = np.sin(rows * (i + 1) + columns * (j + 1));
      if mas[i][j] < 0:
        mas[i][j] = 0; 
  for i in range(0, rows):
    for j in range(0, columns):
      if j == colmin:
        mas[i][colmin], mas[i][colmax] = mas[i][colmax], mas[i][colmin] 
  
  print(mas);

rows = int(input("Введите число строк в матрице:"));
columns = int(input("Введите число столбцов в матрице:"));

col1 = int(input("Введите номер одного столбца в матрице:"));
col2 = int(input("Введите номер другого столбца в матрице:"));

mas(rows, columns, col1, col2);