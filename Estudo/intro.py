import os
from random import randint
from modulos.biblioteca import z

x = 5
print(f"O valor de x é {x}")

for _ in range(5):
    y = randint(5,12)
    print(y)

# os.system("cls")

x = y + z
print(f"aa: {x}")

texto = "Calor"
print(texto[0]) # C
print(texto[1:4]) # alo
print(texto[:3]) # Cal
print(texto[1:]) # alor

# Passe por cada letra de uma palavra e indique o nº de vogais da mesma
texto = "Tiago Daniel da Silva Dias"
num_vogais = 0
for letra in texto:
    if letra.upper() in "AEIOU":
        num_vogais += 1
print(num_vogais)