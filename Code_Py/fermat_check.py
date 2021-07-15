def fermat_check(n):
    cnt = 0
    for a in range(2, n):
        if pow(a, n-1, n) != 1:
            cnt += 1
    return cnt


print(fermat_check(71))
