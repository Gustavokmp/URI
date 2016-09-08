num = int(input())
cont = 0
quantc = 0
quantr = 0
quants = 0
total = 0
while cont < num:
    cobaia = input().split()
    quant = int(cobaia[0])
    tipo = cobaia[1]
    if tipo == "C":
        quantc = quant + quantc
    if tipo == "R":
        quantr = quant + quantr
    if tipo == "S":
        quants = quant + quants
    cont += 1
total =(quantc + quantr + quants)
print("Total: %d cobaias" % (total))
print("Total de coelhos:",quantc)
print("Total de ratos:",quantr)
print("Total de sapos:",quants)
print("Percentual de coelhos: %.2f" % ((quantc/total)*100)+" %")
print("Percentual de ratos: %.2f" % ((quantr/total)*100)+" %")
print("Percentual de sapos: %.2f" % ((quants/total)*100)+" %")
