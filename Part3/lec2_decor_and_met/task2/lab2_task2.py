def decorator(func):
    def wrapped(*args, **kwargs):
        if args[-1] == "+":
            return args[0] + args[1]

        elif args[-1] == "-":
            return args[0] - args[1]

        elif args[-1] == "*":
            return args[0] * args[1]

        elif args[-1] == "/":
            if args[1] == 0:
                return "На ноль делить нельзя!"
            else:
                return args[0] / args[1]
    return wrapped


@decorator
def function(num1, num2, sign):
  print("Фигня какая-то!")
  
print(function(2,0, '-'))