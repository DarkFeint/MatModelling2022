x = int(input("Введите количество элементов ряда Фибоначчи:"))
prev, next = 1, 1;
count = 1;
while count <= x + 1:
  print(prev, end = " ");
  prev, next = next, prev+next;
  count += 1;