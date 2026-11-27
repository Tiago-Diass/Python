from livro import Livro

def carregar_livros(nomeFicheiro):
    with open(nomeFicheiro, "r") as f:
        conteudo = f.readlines()
        listaLivros = []
        for lin in conteudo:
            linha = lin.split(";")
            if linha[3].strip() == "0":
                estado = "emprestado"
            else:
                estado = "disponivel"
            livro = Livro(linha[0], linha[1], int(linha[2]), estado)
            listaLivros.append(livro)
        return listaLivros

def contar_disponiveis(lista):
    livrosDisponiveis = 0
    for livro in lista:
        if livro.estado == "disponivel":
            livrosDisponiveis += 1
            print(livro)
    print(f"Quantidade de livros disponeveis: {livrosDisponiveis}")

def novo_livro():
    print("Informacoes do novo livro")
    nomeLivro = input("Nome do livro: ")
    nomeAutor = input("Nome do autor: ")
    anoLivro = int(input("Ano do livro: "))
    novo_livro = Livro(nomeLivro, nomeAutor, anoLivro)
    return novo_livro

def procurar_por_autor(lista, autor):
    for livro in lista:
        if livro.autor.upper() == autor:
            print(livro)
            livrosAutor = True

    return livrosAutor