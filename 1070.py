a = 1
b = int(input())
c = 0
while a <= 6:
    if (b%2) == 0:
        c = b + 1
        print(c)
    else:
        c = b
        print (c)
        c += 2
    a += 1
    b += 2
