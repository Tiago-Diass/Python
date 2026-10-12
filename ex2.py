from random import randint

notas = []
aprovados = 0
reprovados = 0
nota_alta = 0
perc_aprovado = 0

for _ in range(15):
    n = randint(0,20)
    notas.append(n)
    print(n)

print(f"Nota mais alta: {max(notas)}")
print(f"Nota mais baixa: {min(notas)}")
media = round(sum(notas)/len(notas),2)
print(f"Media das notas: {media}")

for a in range(len(notas)):
    if notas[a] > 10:
        aprovados += 1
    else:
        reprovados += 1

    if notas[a] >= 16:
        nota_alta += 1

print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
print(f"Notas altas: {nota_alta}")

perc_aprovado = (aprovados / len(notas)) * 100
print(f"Percentagem de aprovados: {round(perc_aprovado,2)}")