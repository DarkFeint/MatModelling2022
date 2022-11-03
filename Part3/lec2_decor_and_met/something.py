from datetime import datetime as dt
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        time1 = dt.now()
        list = func(*args, **kwargs)
        time2 = dt.now()
        result = (time2 - time1).total_seconds()
        print(f"Время исполнения функции {func.__name__} составляет {result} секунд")
        return list
    return wrapped


@logger
def make_list1(n):
    list = []
    for i in range(0, n, 2):
        list.append(i)
    #print(*list)
    return list

  
@logger
def make_list2(n):
    list = [x for x in range(0, n, 2)]
    #print(*list)
    return list


count = 100000
make_list1(count)
make_list2(count)

    


