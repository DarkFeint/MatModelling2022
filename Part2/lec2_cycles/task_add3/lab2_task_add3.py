num = int(input("Введите число:"))
num0 = num;
numfin = 0;
lastnum = 0;
count  = 0;
while num0 > 0:
   num0 = num0 // 10;
   count += 1;
while count > 0:
  lastnum = num % 10;
  numfin += lastnum * 10 ** (count - 1);
  count -= 1;
  num = num // 10;
print(numfin)