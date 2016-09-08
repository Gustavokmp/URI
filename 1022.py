from fractions import Fraction

qtd = int(input())
cont = 0
while cont < qtd:
    entrada = input().split()
    n1 =int(entrada[0])
    d1 = int(entrada[2])
    n2 = int(entrada[4])
    d2 = int(entrada[6])
    operacao = entrada[3]

    if(operacao == "+"):
        n = (n1*d2)+(n2*d1)
        d = d1*d2
    elif (operacao == "-"):
        n = (n1*d2)-(n2*d1)
        d = d1*d2
    elif (operacao == "*"):
        n = (n1*n2)
        d = d1*d2
    elif (operacao == "/"):
        n = n1*d2
        d = n2*d1
    simplifica = str(Fraction(n,d))
    verificador = False
    for i in range(len(simplifica)):
        if simplifica[i] == "/":
            verificador = True
    if not verificador:
        simplifica = simplifica+"/1"
    print(str(n)+"/"+str(d)+" =",simplifica)
    cont += 1
        
