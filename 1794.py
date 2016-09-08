num = int(input())
lista1 = input().split()
la = int(lista1[0])
lb = int(lista1[1])
lista2 = input().split()
sa = int(lista2[0])
sb = int(lista2[1])
if la <= num <= lb and sa <= num <= sb:
    print("possivel")
else:
    print("impossivel")
