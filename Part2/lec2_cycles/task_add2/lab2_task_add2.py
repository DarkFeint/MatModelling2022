a = int(input("Введите длину первого отрезка:"))
b = int(input("Введите длину второго отрезка:"))
c = int(input("Введите длину третьего отрезка:"))
count = 0;
if (a <= 0) or (b <= 0) or (c <= 0):
  count = 1;
else:
  if (a + b <= c) or (b + c <= a) or (a + c <= b):
    count = 1;
  else:
    if (a == b) or (b == c) or (a == c):
      if (a == b) and (a == c):
        print("Треугольник является равносторонним.")
      else:
        print("Треугольник является равнобедренным.")
    else:
      print("Треугольник является разносторонним.")
if count == 1:
  print("Такого треугольника не существует.")