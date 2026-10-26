aluno = {"nome": "Ana Silva",
        "idade": 17,
        "disciplinas": ["Matemática", "Física", "Informática"],
        "notas": {"Matemática": 18, "Física": 17, "Informática": 19}
        }

# 1
aluno["disciplinas"].append("Portugues")
aluno["notas"]["Portugues"] = 16

# 2
aluno["idade"] = 18

print(aluno)

# 3
print(f"Notas do aluno {aluno["notas"]}")

# 4
soma_notas = 0.0
media_notas = 0.0

for nota in aluno["notas"].values():
    soma_notas += nota

media_notas = soma_notas / len(aluno["notas"])

print(f"A media das notas é de {media_notas} valores")