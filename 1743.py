n1 = input().split()
n2 = input().split()
cont = 0
x = 0
a = 0
op = 0
while cont < 5:
    y = int(n1[x])
    b = int(n2[a])
    if y == b:
        op += 1   
    cont += 1
    x += 1
    a += 1
if op == 0:
    print("Y")
else:
    print("N")
