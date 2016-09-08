numero = int(input())
acumulador = ""
cont = 0
resto = 10
div = 1
posicao = 0
tamanho = str(numero)
while cont < len(tamanho):
    posicao = int((numero%resto)/div)
    acumulador += str(posicao)
    div *= 10
    resto *= 10
    cont += 1
print(acumulador)
    
