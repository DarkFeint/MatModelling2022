numend = int(input("Введите число:"))
def perfect(num):
  for number in range(1, num):
    num0 = number;
    
    for divider in range(1, (number//2) + 1):
      if number % divider == 0:
        num0 -= divider;
    if num0 == 0:
      print(number)

perfect(numend)