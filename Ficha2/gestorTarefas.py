import os
os.system("clear")

tarefas = []
resposta = ""

while True:
    print("Oque quer fazer?")
    print("1- Ver lista de tarefas")
    print("2- Adicionar tarefa")
    print("3- Adicionar tarefa em posição especifica")
    print("4- Remover tarefa por nome")
    print("5- Remover ultima tarefa")


    resposta = input(print("Insira o número: "))


    if resposta == 1:
        print("a")