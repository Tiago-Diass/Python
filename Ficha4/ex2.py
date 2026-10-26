nome = "Tiago Dias"

contagem = {}

for letra in nome:
    letra = letra.lower()

    if letra.isspace() == False:
        if letra in contagem.keys():
            contagem[letra] += 1
        else:
            contagem[letra] = 1

print(contagem)