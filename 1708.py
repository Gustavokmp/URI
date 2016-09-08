entrada = input().split()
v1 = int(entrada[0])
v2 = int(entrada[1])

voltas = 1
diferenca = v2 - v1

while diferenca < v2:
	diferenca += v2-v1
	
	voltas += 1
	
print(voltas)
