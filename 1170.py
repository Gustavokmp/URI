soma = 0
cont = 0
dia = 0
rep = int(input())
while cont < rep:
    num = float(input())
    while num > 1:
        num = num / 2
        dia += 1
    print(dia,"dias")
    dia = 0
    cont += 1    
    
