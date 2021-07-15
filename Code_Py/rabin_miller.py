import random


def squeeze_q(n):
    k = 0
    x = n-1
    while x % 2 != 1:
        k += 1
        x //= 2
    return (n-1)//pow(2, k), k


def rabin_miller(n, repeat=10):
    if n < 2:
        return "give me more than 1."
    if n == 2:
        return "prime"
    if n % 2 == 0:
        return "composite"
    q, k = squeeze_q(n)
    cnt = 0
    while cnt < repeat:
        a = random.randint(2, n-1)
        cond_1 = pow(a, q, n) != 1
        temp = []
        for i in range(k):
            y = pow(2, i) * q
            c = pow(a, y, n) != n - 1
            temp.append(c)
        cond_2 = all(temp)
        if cond_1 and cond_2:
            return "composite"
        cnt += 1
    return "probably prime"


print(rabin_miller(71))
