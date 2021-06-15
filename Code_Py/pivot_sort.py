import random
import time 

def performance_check(method, data, num=3):
    s = time.time()
    for i in range(num):
        method(data)
    e=time.time()
    return e-s

def quick_sort(array):
    if not array:
        return array
    pivot = random.choice(array)
    left = []
    right = []
    pivots = []
    for v in array:
        if v < pivot:
            left.append(v)
        elif v == pivot:
            pivots.append(v)
        else:
            right.append(v)

    return quick_sort(left) + pivots + quick_sort(right)

my_array = [random.randint(0, 100) for i in range(15)]

print(quick_sort(my_array))
print(performance_check(quick_sort, my_array))
