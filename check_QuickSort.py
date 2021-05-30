import time
import random


def performance_check(method, data, num=3):
    s = time.time()
    for i in range(num):
        method(data)
    e=time.time()
    return e-s

def quick_sort4_7(array):
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

    return quick_sort4_7(left) + pivots + quick_sort4_7(right)

def quick_sort4_5(array):
    if array == []:
        return array

    P = array[-1]
    left = []
    right = []
    pivots = []
    for v in array:
        if v < P:
            left.append(v)
        elif v == P:
            pivots.append(v)
        else:
            right.append(v)

    return quick_sort4_5(left) + pivots + quick_sort4_5(right)


my_array = [random.randint(0, 100) for i in range(15)]

print("Code4.7の実行結果:", quick_sort4_7(my_array))
print("Code4.5の実行結果:", quick_sort4_5(my_array))
print("Code4.7の実行時間:", performance_check(quick_sort4_7, my_array))
print("Code4.5の実行時間:", performance_check(quick_sort4_5, my_array))


