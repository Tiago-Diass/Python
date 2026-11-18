def saudacao(nome: str, curso = "GPSI") -> int:
    print(f"Bem vindo ao Curso de {curso}, {nome}!")

saudacao("Tiago")

hoteis = ...

def funcao():
    global hoteis

def criar_lista(*alunos): # *alunos, aqui o operador * indica que a função pode receber varios argumentos
    lista = []
    for aluno in alunos:
        lista.append(aluno)
    return lista
    # return [aluno1,aluno2]

x = criar_lista("Ana", "João")
y = criar_lista("Rui", "Maria", "Fernando", "Joana", "Isa")
z = ["A1", "A2", "A3", "A4"]
nova_lista = criar_lista(*z) # Desempacotamento da lista z com o operador *
print(x,y,nova_lista)

def config(**configuracoes): # **configuracoes, aqui o operador ** indica que a função pode receber uma chave e um valor, ou seja, um dicionario
    for chave, valor in configuracoes.items():
        print(f"{chave}: {valor}")

config(memoria = "16GB", disco = "SSD 256GB", sistema = "Windows 11")

dicionario = {"memoria": "8GB", "disco": "SSD 512GB", "sistema": "Ubuntu"}
print()
config(**dicionario) # Desempacotamento do dicionario com o operador **

def maiores_dois_valores(n1,n2,n3):
    maior = n1
    maior2 = 0
    if n2 > n1 and n2 > n3:
        maior = n2
        if n1 > n3:
            maior2 = n1
        else:
            maior2 = n3

    return (maior, maior2)

print(maiores_dois_valores(10, 20, 30))