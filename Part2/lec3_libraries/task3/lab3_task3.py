import numpy as np
import lab3_task1 as Pc

def table(x0, y0, v0):
  mas = np.arange(18).reshape(6, 3);
  print("\t t\t x\t y")
  for t in range(0, 6):
    mas[t][0] = t;
    mas[t][1] = x0 + v0 * t;
    mas[t][2] = y0 + v0 * t - Pc.g * t ** 2 / 2;
  print(mas);

x0 = int(input("Введите первую начальную координату:"));
y0 = int(input("Введите вторую начальную координату:"));
v0 = int(input("Введите начальную скорость:"));

table(x0, y0, v0);