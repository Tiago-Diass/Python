import os
os.system("clear")

resposta = 0
tarefas = ["abc", "def", "ghi"]
ad_tarefa = ""
pos_tarefa = 0
rem_tarefa_nome = ""
rem_tarefa = 0

while resposta != 13:
    print("Oque quer fazer?")
    print("1- Ver lista de tarefas")
    print("2- Adicionar tarefa")
    print("3- Adicionar tarefa em posição especifica")
    print("4- Remover tarefa por nome")
    print("5- Remover ultima tarefa")
    print("6- Remover todas as tarefas")
    print("13- Sair")


    resposta = int(input("Insira o número: "))


    match resposta:
        case 1:
            print(tarefas)
        case 2:
            ad_tarefa = input("Qual o nome da tarefa: ")
            tarefas.append(ad_tarefa)
        case 3:
            ad_tarefa = input("Qual o nome da tarefa: ")
            pos_tarefa = int(input("Qual a posição da tarefa: "))
            tarefas.insert(pos_tarefa, ad_tarefa)
        case 4:
            rem_tarefa_nome = input("Qual o nome da tarefa: ")
            tarefas.remove(rem_tarefa_nome)
        case 5:
            print("1- Remover ultima tarefa")
            print("2- Remover tarefa posição espeçifica")
            rem_tarefa = int(input("Qual queres fazer: "))
            if rem_tarefa == 1:
                tarefas.pop()
            if rem_tarefa == 2:
                rem_tarefa = int(input("Qual a posição: "))
                tarefas.pop(rem_tarefa)
        case 6:
            tarefas.remove(len)