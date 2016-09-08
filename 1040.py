valores = input()
notas = valores.split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = (((n1*2)+(n2*3)+(n3*4)+(n4*1))/10)
if media >= 7:
    print ("Media: %.1f" % media)
    print ("Aluno aprovado.")
elif media < 5:
    print("Media: %.1f" % media)
    print ("Aluno reprovado.")
else:
    nota = float(input())
    print("Media: %.1f" % media)
    print ("Aluno em exame.")
    print ("Nota do exame: %.1f" % nota)
    mediaf = ((media + nota) / 2)
    if mediaf >= 5:
        print("Aluno aprovado.")
        print("Media final: %.1f" % mediaf)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % mediaf)
        
