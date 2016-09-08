X = int(input())
Y = int(input())
valor = 0
if X > Y:
    while Y < X:
        Y = Y +1
        if (Y%2) != 0 and Y != X:
            valor = valor + Y
if Y > X:
    while X < Y:
        X = X+1
        if (X%2) != 0 and X != Y:
            valor = valor + X
print(valor)
