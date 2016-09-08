x = int(input())
y = int(input())
if x < y:
    if (x%5) == 2 or (x%5) == 3:
        x += 1
    while x < y:
        if (x%5) == 2 or (x%5) == 3:
            print(x)
        x += 1
if x > y:
    if (y%5) == 2 or (y%5) == 3:
        y += 1
    while y < x:
        if (y%5) == 2 or (y%5) == 3:
            print(y)
        y += 1
