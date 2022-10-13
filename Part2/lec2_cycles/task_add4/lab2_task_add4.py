x = int(input("Введите натуральное число:"))
def mult(num):
  while num > 1:
    for i in range (2, num+1):
      while num % i == 0:
        print(i)
        num = num / i;

mult(x)