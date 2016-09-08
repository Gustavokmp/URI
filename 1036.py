valores = input()
numeros = valores.split()
a = float(numeros[0])
b = float(numeros[1])
c = float(numeros[2])
if a <= 0:
    print("Impossivel calcular")
elif (b**2)-(4*(a*c)) < 0:
    print("Impossivel calcular")
else:
    formula1 = (((-1*b) + ((((b**2) - (4 * (a * c))))**0.5))/(2*a))
    formula2 = (((-1*b) - ((((b**2) - (4 * (a * c))))**0.5))/(2*a))
    print("R1 = %.5f" % formula1)
    print("R2 = %.5f" % formula2)
