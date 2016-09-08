cont = 1
quantidade = int(input())
dentro = 0
fora = 0
if quantidade < 10000:
    while cont <= quantidade:
        X = int(input())
        if (-10**7) < X < (10**7):
            if 10 <= X <= 20:
                dentro += 1
            else:
                fora += 1
            cont += 1
    print (dentro,"in")
    print (fora,"out")
