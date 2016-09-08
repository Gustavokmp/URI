N = int(input())
cont = 1
n1 = 0
while cont <= N and n1 < N:
    if (N%2) == 0:
        n1 += 2
    print (str(n1)+ "^2 =",(n1**2))
    cont += 1
