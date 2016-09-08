cont = 0
while cont < 10:
    x = int(input())
    if x <= 0:
        x = 1
    print("X[" + str(cont) + "] = " + str(x))
    cont += 1
