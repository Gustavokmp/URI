lista = input()
parte = lista.split()
a = int(parte[0])
b = int(parte[1])
c = int(parte[2])
maior1 = (((a+b)+abs(a-b))/2)
maior2 = (((b+c)+abs(b-c))/2)
troca1 = int(maior1)
troca2 = int(maior2)
if troca1 > troca2:
    print(str(troca1) + " eh o maior")
else:
    print(str(troca2) + " eh o maior")
