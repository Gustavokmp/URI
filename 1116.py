cont = 0
quant = int(input())
while cont < quant:
    num = input().split()
    x = int(num[0])
    y = int(num[1])
    if x != 0 and y == 0:
        print("divisao impossivel")
    else:
        print("%.1f" % (x/y))
    cont += 1
