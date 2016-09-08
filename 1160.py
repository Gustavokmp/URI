import math

qtdComparacoes = 0
cidadea = 0
cidadeb = 0 
taxaa = 0
taxab = 0
qtdComparacoes = int(input())

while(qtdComparacoes > 0):
    cidadea, cidadeb, taxaa, taxab = input().split()
    cidadea, cidadeb, taxaa, taxab = float(cidadea), float (cidadeb), float(taxaa), float(taxab)
    
    continua = True
    anos = 0

    while(continua ):
        cidadea += (taxaa * cidadea) / 100
        cidadeb += (taxab * cidadeb) / 100
        cidadea = math.floor(cidadea)
        cidadeb = math.floor(cidadeb)

        if(cidadea > cidadeb):
            continua = False
        if(anos > 100):
            continua = False
        anos += 1
        
    qtdComparacoes -= 1
    if(anos > 100):
        print("Mais de 1 seculo.")
    else:
        print (str(anos)+ " anos.")