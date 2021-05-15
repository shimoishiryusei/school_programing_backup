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

n_len = int(input("配列の要素数："))
li = [int(input()) for _ in range(n_len)]

print(selection_sort(li))

