num = input()
pedido = num.split()
a = int(pedido[0])
b = int(pedido[1])
if a == 1:
    print ("Total: R$ %.2f" %(float(b*4.00)))
elif a == 2:
    print ("Total: R$ %.2f" %(float(b*4.50)))
elif a == 3:
    print ("Total: R$ %.2f" %(float(b*5.00)))
elif a == 4:
    print ("Total: R$ %.2f" %(float(b*2.00)))
else:
    print ("Total: R$ %.2f" %(float(b*1.50)))
