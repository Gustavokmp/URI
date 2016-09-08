qtd = int(input())
cont = 0
pokemons = 151
pegou = [""]
while cont < qtd:
    pokemon = input()
    repetido = False
    for i in pegou:
        if pokemon == i:
            repetido = True
            break
    if not repetido:
        pegou.append(pokemon)
        pokemons -= 1
            
        
    cont += 1
print("Falta(m)",pokemons ,"pomekon(s).")
