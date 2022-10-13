a = int(input("Введите первый коэффициент:"));
b = int(input("Введите второй коэффициент:"));
c = int(input("Введите третий коэффициент:"));

dis = b ** 2 - 4 * a * c;
if a != 0:
  
  if b > 0:
    if c > 0:
      print(f"{a}*x^2 + {b}*x + {c} = 0");


    elif c == 0:
      print(f"{a}*x^2 + {b}*x = 0");


    else:
      print(f"{a}*x^2 +{b}*x - {abs(c)} = 0");


  elif b == 0:
    if c > 0:
      print(f"{a}*x^2 + {c} = 0");


    elif c == 0:
      print(f"{a}*x^2 = 0");


    else:
      print(f"{a}*x^2 - {abs(c)} = 0");


  else:
    if c > 0:
      print(f"{a}*x^2 - {abs(b)}*x + {c} = 0");


    elif c == 0:
      print(f"{a}*x^2 - {abs(b)}*x = 0");


    else:
      print(f"{a}*x^2 - {abs(b)}*x - {abs(c)} = 0");
  if dis < 0:
    print("Это уравнение не имеет решений вовсе.");
  elif dis == 0:
    x = - b / (2 * a);
    print(f"Корень уравнения равен {x}.");
  elif dis > 0:
    x1 = (- b + dis **(1/2))/ (2 * a);
    x2 = (- b - dis **(1/2))/ (2 * a);
    print(f"Корни уравнения равны {x1} и {x2}.");
else:
  if b > 0:
    if c > 0:
      print(f"{b}*x + {c} = 0");


    elif c == 0:
      print(f"{b}*x = 0");


    else:
      print(f"{b}*x - {abs(c)} = 0");


  elif b == 0:
    if c > 0:
      print(f"{c} = 0");


    elif c == 0:
      print("0 = 0");


    else:
      print(f"{abs(c)} = 0");


  else:
    if c > 0:
      print(f"{b}*x + {c} = 0");


    elif c == 0:
      print(f"{b}*x = 0");


    else:
      print(f"{b}*x - {abs(c)} = 0");

  if b != 0:
    if c != 0:
      x = -c / b;
    else:
      x = 0;
    print(f"Корень уравнения равен {x}.");
  else:
    if c != 0:
      print("Это уравнение не имеет решений вовсе.");
    else:
      print("Переменная может принимать любое значение.");