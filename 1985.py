cont = 0
num = int(input())
lista = [0]
aprovado = 0
soma = 0
while cont < num:
    pedido = input().split()
    codigo = int(pedido[0])
    quantidade = int(pedido[1])
    aprovado = 0
    for i in lista:
        if i == codigo:
            aprovado += 1
    if aprovado == 0:
        if codigo == 1001:
            soma = soma + (quantidade*1.5)
        elif codigo == 1002:
            soma = soma + (quantidade*2.5)
        elif codigo == 1003:
            soma = soma + (quantidade*3.5)
        elif codigo == 1004:
            soma = soma + (quantidade*4.5)
        elif codigo == 1005:
            soma = soma + (quantidade*5.5)
    cont +=1
            
        
print("%.2f"%soma)
