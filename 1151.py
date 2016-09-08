a = 0
b = 1
soma = "0 "
num = int(input())
cont = 1
while cont < num:
    soma = soma + str(b) + " "
    a,b = b,a+b
    cont += 1
print(soma[0:-1])
