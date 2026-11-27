from functions import *

lista = carregar_livros("livros.txt")

# for livro in lista:
#     print(livro)

contar_disponiveis(lista)

# novo_livro()

autor = "José Saramago".upper()

procurar_por_autor(lista, autor)