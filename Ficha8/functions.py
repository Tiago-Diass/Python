from livro import Livro

def carregar_livros(nomeFicheiro):
    with open("Ficha8/livros.txt", "r") as f:
        linhas = f.readlines()
        listaLivros = []
        for lin in linhas:
            linha = lin.split(";")
            if linha[3].strip() == "0":
                estado = "emprestado"
            else:
                estado = "disponivel"
            livro = Livro(linha[0], linha[1], int(linha[2]), estado)
            listaLivros.append(livro)
        return listaLivros

def contar_disponiveis(lista):
    pass