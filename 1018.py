valor = int(input())
cedulas_de_100 = int(valor/100)
resto_de_100 = (valor % 100)
cedulas_de_50 = int(resto_de_100 / 50)
resto_de_50 = (resto_de_100 % 50)
cedulas_de_20 = int(resto_de_50 / 20)
resto_de_20 = (resto_de_50 % 20)
cedulas_de_10 =int(resto_de_20 / 10)
resto_de_10 = (resto_de_20 % 10)
cedulas_de_5 = int(resto_de_10 / 5)
resto_de_5 = (resto_de_10 % 5)
cedulas_de_2 = int(resto_de_5 / 2)
resto_de_2 = (resto_de_5 % 2)
cedulas_de_1 = int(resto_de_2 / 1)
print(valor)
print(cedulas_de_100,"nota(s) de R$ 100,00")
print(cedulas_de_50,"nota(s) de R$ 50,00")
print(cedulas_de_20,"nota(s) de R$ 20,00")
print(cedulas_de_10,"nota(s) de R$ 10,00")
print(cedulas_de_5,"nota(s) de R$ 5,00")
print(cedulas_de_2,"nota(s) de R$ 2,00")
print(cedulas_de_1,"nota(s) de R$ 1,00")
