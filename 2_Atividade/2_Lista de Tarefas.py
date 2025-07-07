lista = []

print("================================")
print("      MINHA LISTA DE TAREFAS    ")
print("================================")
print("Escolha uma opção: ")
print("1. Adicionar nova tarefa")
print("2. Ver todas as tarefas")
print("3. Sair")
print("--------------------------------")
opcao = int(input("Sua escolha: "))
if opcao == 2 :
    if lista == [] :
     print("--------------------------------")
     print("Não tem nada na lista")
     print("--------------------------------")
    else :
        numero_da_tarefa = 1
        for tarefa in lista :
            print(f"{numero_da_tarefa}. {tarefa}")
            numero_da_tarefa += 1
elif opcao == 1 :
    tarefa = input("Digite a descrição da nova tarefa: ")
    lista.append(tarefa)
    print("Tarefa", tarefa, "adicionada com sucesso!")
while opcao != 3 :
    print("================================")
    print("      MINHA LISTA DE TAREFAS    ")
    print("================================")
    print("Escolha uma opção: ")
    print("1. Adicionar nova tarefa")
    print("2. Ver todas as tarefas")
    print("3. Sair")
    print("--------------------------------")
    opcao = int(input("Sua escolha: "))
    if opcao == 2 :
            if lista == [] :
                print("--------------------------------")
                print("Não tem nada na lista")
                print("--------------------------------")
            else :
                numero_da_tarefa = 1
                for tarefa in lista :
                    print(f"{numero_da_tarefa}. {tarefa}")
                    numero_da_tarefa += 1
    elif opcao == 1 :
            tarefa = input("Digite a descrição da nova tarefa: ")
            lista.append(tarefa)
            print("Tarefa", tarefa, "adicionada com sucesso!")