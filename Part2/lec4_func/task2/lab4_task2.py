import numpy as np
def mult(mas):
  mult = 1
  for i in range(len(mas)):
    mult = mult * mas[i];
  return mult

mas = np.array(list(map(int, input().split())))
print(mult(mas))