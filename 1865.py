cont = 0
num = int(input())
while cont < num:
    tentativa = input().split()
    nome = tentativa[0]
    if nome == "Thor":
        print("Y")
    else:
        print("N")
    cont += 1
