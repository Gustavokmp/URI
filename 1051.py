salario = float(input())
if salario <= 2000:
    print("Isento")
if 2000 < salario <= 3000:
    print("R$ %.2f" % ((salario - 2000) * 0.08))
if 3000 < salario <= 4500:
    print("R$ %.2f" % (((salario - 3000)*0.18)+80))
if salario > 4500:
    print("R$ %.2f" % (((salario - 4500)*0.28)+350))
