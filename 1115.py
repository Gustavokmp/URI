cont = 0
while cont < 1:
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    if x > 0 and y > 0:
        print("primeiro")
    if x < 0 and y > 0:
        print("segundo")
    if x < 0 and y < 0:
        print("terceiro")
    if x > 0 and y < 0:
        print("quarto")
    if x == 0 or y == 0:
        cont += 1
