salario = float(input())
if 0 <= salario <= 400.00:
    porcentagem = ( salario * (15/100))
    salario_novo = (salario + porcentagem)
    percentual = "15 %"
if salario > 400.00 and salario < 800.00:
    porcentagem = (salario * (12/100))
    salario_novo = (salario + porcentagem)
    percentual = "12 %"
if salario > 800.00 and salario <= 1200.00:
    porcentagem = (salario * (10/100))
    salario_novo = (salario + porcentagem)
    percentual = "10 %"
if salario > 1200.00 and salario <= 2000.00:
    porcentagem = (salario * (7/100))
    salario_novo = (salario + porcentagem)
    percentual = "7 %"
if salario > 2000.00:
    porcentagem = (salario * (4/100))
    salario_novo = (salario + porcentagem)
    percentual = "4 %"
print("Novo salario: %.2f" % salario_novo)
print("Reajuste ganho: %.2f" % porcentagem)
print("Em percentual:",percentual)
