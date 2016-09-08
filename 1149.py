lista = []
lista = input().split()

soma = 0
a = 0
b = 0

cont = 0
while(a == 0 or b == 0):
    if(int(lista[cont]) > 0):
        if(a == 0):
            a = int(lista[cont])
        elif(b == 0):
            b = int(lista[cont])
    cont += 1

for i in range(b):   
    soma += a+i
print (soma )