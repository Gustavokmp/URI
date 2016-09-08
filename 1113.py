cont = 0
while cont < 1:
    num = input().split()
    a = int(num[0])
    b = int(num[1])
    if a == b:
        cont += 1
    if a < b:
        print("Crescente")
    if a > b:
        print("Decrescente")
