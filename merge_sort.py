import time
import random


def performance_check(method, data, num=3):
    s = time.time()
    for i in range(num):
        method(data)
    e=time.time()
    return e-s

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid_idx = len(array) // 2
    
    left = array[:mid_idx]
    right = array[mid_idx:]
    
    return merge_arrays(merge_sort(left), merge_sort(right))

def merge_arrays(left, right=[]):
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res + left[i:] + right[j:]

my_array = [random.randint(0, 100) for i in range(15)]

print(merge_sort(my_array))
print("実行時間:", performance_check(merge_sort, my_array))


