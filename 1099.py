num = int(input())
cont = 0
valor = 0
while cont < num:
    numeros = input().split()
    x = int(numeros[0])
    y = int(numeros[1])
    if x > y:
        while y < x:
            y = y+1
            if (y%2) != 0 and y != x:
                valor = valor + y
    if y > x:
        while x < y:
            x = x + 1
            if (x%2) != 0 and x != y:
                valor = valor + x
    print(valor)
    cont += 1
    valor = valor - valor
