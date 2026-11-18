def imprimirLivro(inventario):
    if len(inventario) == 0:
        print("\nO inventário está vazio.")
    else:
        print("\nO seu inventario: ")
        for livro in inventario:
            print(livro)
        x = input("\nEscreva um caractere para continuar...")

def last_id(inventario):
    if len(inventario) == 0:
        return 0
    lista_ids = []
    for livro in inventario:
        lista_ids.append(livro["id"])
    return max(lista_ids)

def adicionarLivro(inventario):
    print("\nAdicionar um Livro ao Inventário")
    id = last_id(inventario) + 1
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    quantidade = int(input("Digite a quantidade do livro: "))
    preco = float(input("Digite o preço do livro: "))
    livro = {"id": id, "titulo": titulo, "autor": autor, "quantidade": quantidade, "preco": preco}
    inventario.append(livro)

def atualizar_stock(id, inventario):
    encontrei = False
    for livro in inventario:
        if livro["id"] == id:
            livro["quantidade"] = int(input("Digite a nova quantidade do livro: "))
            encontrei = True
    if not encontrei:
        print("\nLivro não encontrado.")
