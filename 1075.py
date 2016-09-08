a = int(input())
cont = 1
if 1 < a < 10000:
    while cont < 10000:
        cont += 1
        if (cont%a) == 2:
            print(cont)
