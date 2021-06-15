import random
import timeit

def selection_sort(li):
    l = li.copy()
    n = len(l)

    for i in range(n):
        min_num = i
        for j in range(i,n):
            if l[j] < l[min_num]:
                min_num = j
        l[i], l[min_num] = l[min_num], l[i]

    return l

my_array = [random.randint(0, 99) for i in range(10000)]

print("自作関数: ",timeit.timeit('selection_sort(my_array)', globals=globals(), number=1))


print("sorted: ",timeit.timeit('sorted(my_array)', globals=globals(), number=1))



