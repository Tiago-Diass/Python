import json

f = open("Ficheiros/dados.txt", "r")
lista = f.readlines()
# print(lista)

# for linha in lista:
#     print(linha.strip())

f.close()

with open("Ficheiros/dados.txt", "r") as f:
    lista = f.readlines()
    for linha in lista:
        print(linha.strip())

with open("Ficheiros/nomes.txt", "w") as file:
    file.write("Goncalo\n")
    file.write("Tiago\n")

with open("Ficheiros/nomes.txt", "a") as file:
    file.write("Dinis\n")
    file.write("Davi\n")

with open("Ficheiros/nomes.json", "r") as f:
    dados = json.load(f)

print(dados)
nome = {"nome": "Maria Joana", "idade": 67}
dados.append(nome)

with open("Ficheiros/nomes.json", "w") as f:
    json.dump(dados,f,indent=4)

print(dados)