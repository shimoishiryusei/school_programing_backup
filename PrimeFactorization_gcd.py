def PrimeFactorization_gcd(a,b):
    anum_l = []
    bnum_l = []
    nums = []
    x = 1
    for i in range(2, a+1):
        while True:
            if a % i == 0:
                anum_l.append(i)
                a = a // i
            else:
                break

    for j in range(2, b+1):
        while True:
            if b % j == 0:
                bnum_l.append(j)
                b = b // j
            else:
                break

    for i in anum_l:
       if i in bnum_l:
           nums.append(i)
           bnum_l.remove(i)

    for i in nums:
        x *= i

    return x

a = int(input())
b = int(input())

print(PrimeFactorization_gcd(a,b))
