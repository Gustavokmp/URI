cont = 1
maior = 0
menor = 0
cont2 = 0
while cont <= 100:
    a = int(input())
    if a > maior:
        menor = maior
        maior = a
        cont2 = cont
    cont += 1
print(maior)
print(cont2)
