a = 1
b = int(input())
c = 1
while a <= b and c <= b:
    if (b%2) == 1:
        print(c)
        c += 2
    else:
        b -= 1
    a += 1
        
    