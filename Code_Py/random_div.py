import random


def random_div(n, repeat=10):
    if n % 2 == 0:
        return "composite"
    d_max = int(pow(n, 0.5))
    odd_seq = range(3, d_max+1, 2)
    for cnt in range(repeat):
        d = random.choice(odd_seq)
        if n % d == 0:
            return "composite"
    return "probably prime"


print(random_div(71))
for i in range(20):
    print(random_div(1105))
