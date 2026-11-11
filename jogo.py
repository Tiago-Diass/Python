from random import randint

jogador = {
    "vida": 300, 
    "ataque": 20, 
    "pocoesCura": 2, 
    "pontosRecuperados": 0,
    "inimigosDerrotados": 0
    }

inimigos = [
    {
        "nome": "Goblin",
        "vida": 40,
        "ataque": 8,
        "pontos": 100
        },
    {
        "nome": "Orc",
        "vida": 55,
        "ataque": 11,
        "pontos": 200
        },
    {
        "nome": "Troll",
        "vida": 70,
        "ataque": 14,
        "pontos": 300
        },
    {
        "nome": "Beast",
        "vida": 85,
        "ataque": 17,
        "pontos": 400
        },
    {
        "nome": "Dragão",
        "vida": 100,
        "ataque": 20,
        "pontos": 500
        }
]


def definir_inimigos():  
    inimigosPartida = []

    for _ in range(randint(3, 5)):
        inimigosPartida.append(inimigos[randint(0, len(inimigos)-1)].copy())

    return inimigosPartida


def atacarInimigos(inimigosPartida):
    if len(inimigosPartida) == 0:
        print("Derrotaste todos os inimigos! Ganhaste o Jogo")
        return 0
    
    print(f"Inimigos da Partida Restantes: ")
    for i in range(len(inimigosPartida)):
        print(f"{i} - {inimigosPartida[i]}")

    escolha = int(input("Qual o inimigo que queres atacar pelo numero: "))
    if escolha < 0 or escolha > len(inimigosPartida):
        while escolha < 0 or escolha > len(inimigosPartida):
            print(f"Apenas numeros entre 0 e {len(inimigosPartida)}")
            escolha = int(input("Qual o inimigo que queres atacar pelo numero: "))

    if escolha >= 0 and escolha <= len(inimigosPartida):
        inimigosPartida[escolha]["vida"] -= randint(10, jogador["ataque"])
        if inimigosPartida[escolha]["vida"] < 0:
            inimigosPartida[escolha]["vida"] = 0

        if inimigosPartida[escolha]["vida"] == 0:
            print(f"Você derrotou o { inimigosPartida[escolha]['nome'] } e ganhou { inimigosPartida[escolha]['pontos'] } pontos!")
            jogador["pontosRecuperados"] += inimigosPartida[escolha]["pontos"]
            jogador["inimigosDerrotados"] += 1
            inimigosPartida.pop(escolha)
        else:
            print(f"Você atacou o {inimigosPartida[escolha]['nome']} e agora ele tem {inimigosPartida[escolha]["vida"]} pontos de vida")
            jogador["vida"] -= randint(5, inimigosPartida[escolha]["ataque"])
            if jogador["vida"] < 0:
                jogador["vida"] = 0
            print(f"O {inimigosPartida[escolha]['nome']} atacou você e agora tens {jogador["vida"]} pontos de vida")      


def dadosJogador(inimigosPartida):
    print("------Dados do Jogador------")
    print(f"Vida do jogador: {jogador['vida']}")
    print(f"Pontos do jogador: {jogador["pontosRecuperados"]}")
    print(f"Inimigos derrotados: {jogador["inimigosDerrotados"]}")
    print(f"Inimigos ainda vivos: {len(inimigosPartida)}")
    print(f"Numero de poções: {jogador['pocoesCura']}")


def dadosInimigos(inimigosPartida):
    if len(inimigosPartida) > 0:
        print("\n\n------Dados dos Inimigos-------\n")
        for i in range(len(inimigosPartida)):
            print(f"Nome do Inimigo: {inimigosPartida[i]['nome']}")
            print(f"Vida do Inimigo: {inimigosPartida[i]["vida"]}")
            print(f"Ataque do Inimigo: {inimigosPartida[i]['ataque']}")
            print("-------------------")
        print("\n")
    else:
        print("Nao existe inimigos Ativos")


def usarPocao():
    if jogador["vida"] >= 100:
        print("Não podes usar poção, tens mais de 100 pontos de vida")
    elif jogador["pocoesCura"] == 0:
        print("Não tens poções de cura!")
    else:
        jogador["pocoesCura"] -= 1
        jogador["vida"] += 25
        if jogador["vida"] > 100:
            jogador["vida"] = 100
        print(f"Agora tens {jogador['vida']} pontos de vida e {jogador['pocoesCura']} pocoes de cura")


def mensagemFinal(resultado):
    if resultado == "Ganhaste":
        print("Parabéns.. tu ganhaste!")
    elif resultado == "FUGA":
        print("Partida terminada por fuga.")
    else:
        print("Perdeste.. para a próxima corre melhor!")

    resposta = input("Deseja saber seus dados finais(S/N): ")
    if resposta == "S":
        print(jogador)


print("\nBem vindo ao Batalha RPG\n")

def jogo():
    jogoAcabou = False 
    inimigosPartida = definir_inimigos()
    while jogoAcabou != True:
        print(" ======== BATALHA ======== " \
        "\n1 — Atacar inimigo " \
        "\n2 — Consultar estado do jogador " \
        "\n3 — Listar inimigos vivos " \
        "\n4 — Usar poção de cura " \
        "\n5 — Fugir / terminar jogo\n")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                atacarInimigos(inimigosPartida)
            case "2":
                dadosJogador(inimigosPartida)
            case "3":
                dadosInimigos(inimigosPartida)
            case "4":
                usarPocao()
            case "5":
                resultado = "FUGA"
                jogoAcabou = True
            case _:
                print("Opção inexistente no Menu!")
                input("Prima para continuar...")

        if len(inimigosPartida) == 0:
            jogoAcabou = True
            resultado = "Ganhaste"
        if jogador["vida"] <= 0:
            jogoAcabou = True
            resultado = "Perdeste"

    mensagemFinal(resultado)
    return resultado

jogo()