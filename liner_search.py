import time
import random

def performance_check(method, data, target, num=3):
    s = time.time()
    for i in range(num):
        method(data, target)
    e=time.time()
    return e-s


def liner_search(array, target):
    c = 0
    for v in array:
        if v == target:
            return c  
        c += 1
    return False

my_array = [random.randint(0, 100) for i in range(15)]

print(my_array)
target = int(input("target = "))
print(liner_search(my_array, target))
print(performance_check(liner_search, my_array, target))


