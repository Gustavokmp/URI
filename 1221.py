cont = 0
qtd = int(input())
while cont < qtd:
    teste = 0
    num = int(input())
    cont += 1
    if num == 0:
        print("Not Prime")
        continue
    if num == 1:
        print("Not Prime")
        continue
    if num == 2:
        print("Prime")
        continue
    for i in range(2,int((num**0.5)+1)):
        if num%i == 0:
            teste += 1
        if teste == 2:
            break
    if teste >= 1:
        print("Not Prime")
    else:
        print("Prime")
