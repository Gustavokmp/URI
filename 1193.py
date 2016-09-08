cont = 1
qtd = int(input())
while(cont <= qtd):
    teste = input().split()
    tipo = teste[1]
    numero = teste[0]
    if tipo == "bin":
       print("Case "+str(cont)+":")
       decimal=int(numero,2)
       print(decimal,"dec")
       hexdecimal =hex(int(numero,2))
       print(hexdecimal[2:],"hex")
       print()
    if tipo == "dec":
        print("Case "+str(cont)+":")
        hexdecimal =hex(int(numero))
        print(hexdecimal[2:],"hex")
        print(bin(int(numero))[2:],"bin")
        print()
    if tipo == "hex":
        print("Case "+str(cont)+":")
        binario = bin(int(numero, 16))
        print(int(binario[2:],2),"dec")
        print(binario[2:],"bin")
        print()
    cont += 1
