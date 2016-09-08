N = int(input())
cont = 0
while cont != N:
    cont += 1
    X = int(input())
    if X == 0:
        print("NULL")
    elif (X%2) == 0:
        if X > 0 :
            print("EVEN POSITIVE")
        if X < 0:
            print("EVEN NEGATIVE")
    elif (X%2) == 1:
        if X > 0:
            print("ODD POSITIVE")
        if X < 0:
            print("ODD NEGATIVE")