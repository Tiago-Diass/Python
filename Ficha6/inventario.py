from funcoesFicha6 import imprimirLivro, adicionarLivro, atualizar_stock

inventario = [
    {"id": 1, "titulo": "O Crime do Padre Amaro", "autor": "Eça de Queirós", "quantidade": 14, "preco": 15.5},
    {"id": 2, "titulo": "Ensaio sobre a Cegueira", "autor": "José Saramago", "quantidade": 8, "preco": 18.0},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "quantidade": 22, "preco": 14.2}
]

resposta = 0

def app():
    global resposta
    while resposta != 7:
        print("\n------MENU DE GESTAO DE LIVROS-------")
        print("1- Ver Inventário de Livros")
        print("2- Adicionar um Livro ao Inventário")
        print("3- Atualizar um Livro do Inventário")
        print("4- Remover um Livro do Inventário")
        print("5- Pesquisa Avançada")
        print("6- Calcular Stock")
        print("7- Sair\n")
        resposta = int(input("Oque deseja Fazer (1-7): "))

        match (resposta):
            case 1:
                imprimirLivro(inventario)
            case 2:
                adicionarLivro(inventario)
            case 3:
                id = int(input("Digite o ID do livro a ser atualizado: "))
                atualizar_stock(id, inventario)

app()