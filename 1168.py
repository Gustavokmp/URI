qtd = int(input())
cont = 0
while cont < qtd:
    numeros = input()
    acumulador = 0
    for i in range(len(numeros)):
        if int(numeros[i]) == 1:
            acumulador += 2
        elif int(numeros[i]) == 2 or int(numeros[i]) == 3 or int(numeros[i]) == 5:
            acumulador += 5
        elif int(numeros[i]) == 4:
            acumulador += 4
        elif int(numeros[i]) == 6 or int(numeros[i]) == 9 or int(numeros[i]) == 0:
            acumulador += 6
        elif int(numeros[i]) == 7:
            acumulador += 3
        elif int(numeros[i]) == 8:
            acumulador += 7
    print(acumulador,"leds")
    
    cont += 1
