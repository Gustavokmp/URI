cont = 0
soma = 0
cont2 = 0
while cont < 1:
    idade = int(input())
    if idade > 0:
        soma = soma + idade
        cont2 += 1
    if idade < 0:
        cont += 1
print("%.2f" % (soma/cont2))
