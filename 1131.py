cont = 0
vit_inter = 0
vit_gremio = 0
empate = 0
repeticao = 1
while cont < 1:
    gols = input().split()
    inter = int(gols[0])
    gremio = int(gols[1])
    if inter > gremio:
        vit_inter += 1
    if inter < gremio:
        vit_gremio += 1
    if inter == gremio:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    novo = int(input())
    if novo == 1:
        repeticao += 1
    if novo == 2:
        cont += 1
print(str(repeticao) + " grenais")
print("Inter:" + str(vit_inter))
print("Gremio:" + str(vit_gremio))
print("Empates:" + str(empate))
if vit_inter > vit_gremio:
    print("Inter venceu mais")
if vit_gremio > vit_inter:
    print("Gremio venceu mais")
if vit_inter == vit_gremio:
    print("Nao houve vencedor")


    
