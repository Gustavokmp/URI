def primo (num):
    teste = 0
    if num == 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,int((num**0.5)+1)):
        if num%i == 0:
            teste += 1
        if teste == 2:
            break
    if teste >= 1:
        return False
    else:
        return True


cont = 0
num = int(input())
soma = 0
distancia = 60000000
while cont < 10:
    if primo(num):
        soma += num
        cont += 1
    num += 1
print(soma,"km/h")
print(int(distancia/soma),"h /",int((distancia/soma)/24),"d")
