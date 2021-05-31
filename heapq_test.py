import heapq
import random
import timeit


def heap_sort(array):
    heap = []
    for v in array:
        heapq.heappush(heap, v)
        #print(heap)
    return [heapq.heappop(heap) for i in range(len(heap))]

my_array = [random.randint(0, 100) for i in range(15)]

heap_sort(my_array)
print(heap_sort(my_array))
print(timeit.timeit('heap_sort',globals=globals(),number=1))