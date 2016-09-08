soma = 0
num1 = int(input())
num2 = int(input())
if num1 > num2:
    menor = num2
    num2 = num1
    num1 = menor
while num1 <= num2:
    if num1 % 13 != 0:
        soma = soma + num1
    num1 += 1
print(soma)
