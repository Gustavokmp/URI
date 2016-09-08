cont = 0
valor = ""
soma = 0
troca = 0
while cont < 1:
    numeros = input().split()
    a = int(numeros[0])
    b = int(numeros[1])
    if a <= 0 or b <= 0:
        cont += 1
    else:
        if a < b:
            troca = b
            b = a
            a = troca
        if a > b:
            while a >= b:
                valor += (str(b) + " ")
                soma = soma + b
                b += 1
            print(valor + "Sum=" + str(soma))
            valor = ""
            soma = soma - soma
