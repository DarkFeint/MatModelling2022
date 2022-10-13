import numpy as np
import math as m

def mas(rows, columns):
  mas = np.zeros((rows, columns));
  for i in range(0, rows):
    for j in range(0, columns):
      mas[i][j] = m.sin(rows * (i + 1) + columns * (j + 1));
      if mas[i][j] < 0:
        mas[i][j] = 0;
  
  print(mas);

rows = int(input("Введите число строк в матрице:"));
columns = int(input("Введите число столбцов в матрице:"));
mas(rows, columns);