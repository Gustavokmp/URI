a = int(input())
cont = 1
while cont <= a:
    notas = input().split()
    n1 = float(notas[0])
    n2 = float(notas[1])
    n3 = float(notas[2])
    cont +=1
    print("%.1f"%(((n1*2)+(n2*3)+(n3*5))/10))
