# def decorator(func):
#   def wrapper_function(*args, **kwargs):
#     #print(*args, **kwargs)
#     func(*args, **kwargs)
#     print(*args, **kwargs)
#   return wrapper_function


# @decorator
# def greet(name, a = 10):
#   print(f"Привет {name}!")
#   print(f"число {a}")


# greet("Анастасия")

# def logger(func):
#   #def wrapper_function(*args, **kwargs):
#   def wrapper_function(list_of_num):
#     result = func(list_of_num)
#     with open('log.txt', 'w') as f:
#       f.write(str(result))
#     return result
#   return wrapper_function

# @logger
# def summator(list_of_num):
#   return sum(list_of_num)


# summator([1,2,3,4])
# def logger(filename):
#   def decorator(func):
#     def wrapped(*args, **kwargs):
#       result = func(*args, **kwargs)
#       with open(filename, 'w') as f:
#         f.write(str(result))
#       return result
#     return wrapped
#   return decorator

# @logger('file_log.txt')
# def summator(list_of_num):
#   return sum(list_of_num)

# summator([1,2,3,4])

# import functools
# import math

# def debug(func):
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [str(a) for a in args]
#         kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Вызываем функцию {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"Функцию {func.__name__} вернула значение {value}")
#         return value
 
#     return wrapper_debug


# debug_factorial = debug(math.factorial)
 
# def show_debug_function(terms=5):
#     return [debug_factorial(n) for n in range(terms+1)]
 
# show_debug_function(7)

# class MyClass:
#     counts = 0
    
 
#     def __init__(self):
#         MyClass.counts = MyClass.counts + 1
 
#     @classmethod
#     def classmethod(cls):
#         print(cls.counts)
 
 
# MyClass.classmethod()
# mc1 = MyClass()
# mc2 = MyClass()
# mc3 = MyClass()
 
# MyClass.classmethod()
# class SummatorClass:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
 
#     @property
#     def sum_two_num(self):
#         print(f"Сумма двух чисел равна {self.a + self.b}")
 
# sum_cls = SummatorClass(1,2)
# sum_cls.sum_two_num

# class SpaceShip:
#     def __init__(self,weight):
#         self._weight = weight
 
#     weight = property()
 
#     #геттер
#     @weight.getter
#     def weight(self):
#         return self._weight
 
#     #сеттер
#     @weight.setter
#     def weight(self, value):
#         if value <= 100:
#             self._weight = 100
#         elif value > 5000:
#             self._weight = 5000
#         else:
#             self._weight = value


def fignya(num):
    def decorator(func):
        def wrapped(*args, **kwargs):
            return num + func(*args, **kwargs)
        return wrapped
    return decorator
    





@fignya(3)
def number(a):
  return a;


x = 10
print(number(x))
