from heapq import merge
import time
import random
def performance_check(method, data, num=3):
    s = time.time()
    for i in range(num):
        method(data)
    e=time.time()
    return e-s

def merge_sort_heap(array):
    if len(array) <= 1:
        return array
    mid_idx = len(array) // 2
    
    left = array[:mid_idx]
    right = array[mid_idx:]

    left = merge_sort_heap(left)
    right = merge_sort_heap(right)
    return list(merge(left, right))

my_array = [random.randint(0, 100) for i in range(15)]

print(performance_check(merge_sort_heap, my_array))
print(merge_sort_heap(my_array))
