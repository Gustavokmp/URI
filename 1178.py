num = float(input())
cont = 0
div = 2
soma = 0
print("N[" + str(cont) + "] = %.4f" % num)
while cont < 99:
    div = num/2
    soma = div
    cont += 1
    print("N[" + str(cont) + "] = %.4f" % div)
    num = soma
