import numpy as np
def ar_average(mas):
  return np.sum(mas) / len(mas)


mas = np.array(list(map(int, input().split())))
print(ar_average(mas))