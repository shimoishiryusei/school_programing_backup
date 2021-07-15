def make_table(m):
    tmp1 = '{:>5}' * (m+2)
    header = ['a']
    for i in range(1, m+2):
        header.append(i)
    print(tmp1.format(*header))
    for a in range(m):
        vals = [a]
        for i in range(1, m+2):
            vals.append(a**i % m)
        print(tmp1.format(*vals))


make_table(11)
