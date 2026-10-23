# 1
numPares = [i for i in range(1,11) if i % 2 == 0]
print(numPares)

# 2
numQuadrados = [i**2 for i in range(1,11)]
print(numQuadrados)

# 3
palavras = ["ola", "ole", "oliver benji", "Sponge Bob"]
tamPalavra = [len(palavra) for palavra in palavras]
print(tamPalavra)

# 4
nums = [1,2,3,4,5,6,7,8,9,10,67]
numsgrandes = [num for num in nums if num > 5]
print(numsgrandes)

# 5
nome = "MarcelO ViEiRa amorIM"
letrasmaior = [letra for letra in nome if letra == letra.upper() and letra.isspace() == False]
print(letrasmaior)

# 6
nums = [1,2,3,4,5,6,7,8,9,10]
numsmultiplos = [num*2 if num % 3 == 0 else num for num in nums]
print(numsmultiplos)

# 7
nomes = ["jorge", "alberto", "dinis", "afonso", "ajudante de pedreiro"]
nomes_a = [nome.upper() for nome in nomes if nome.startswith("a")]

print(nomes_a)

# 8
frutas = ["maca", "pera", "melancia", "abacaxi"]
comprimentofruta = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]

# for fruta in frutas:
#     if len(fruta) > 5:
#         comprimentofruta.append(len(fruta))
#     else:
#         comprimentofruta.append(0)

print(comprimentofruta)