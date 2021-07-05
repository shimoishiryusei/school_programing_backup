import random
import time
import sys


def rand_n_digit_int(n):
    return random.randint(10**(n-1), 10**n - 1)


def create_n_list(n):
    s = time.time()
    test_list = [random.random() for i in range(rand_n_digit_int(n))]
    e = time.time()
    return e - s, sys.getsizeof(test_list)


for i in range(1, 9):
    t, s = create_n_list(i)
    print(f'{i}\t{t}\t{s/1024/1024}')
