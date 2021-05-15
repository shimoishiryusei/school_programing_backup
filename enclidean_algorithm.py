def euclidean(a,b):
    x = 0

    while(True):
        r = a % b

        if r == 0:
            x = b
            break
        else:
            a = b
            b = r

    return x

a = int(input())
b = int(input())

print(euclidean(a,b))

        
