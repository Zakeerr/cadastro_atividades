from src.service.gerenciador_service import GerenciadorService

service = GerenciadorService()


def mostrar_menu():
    print("\n=== ORGANIZAJÁ ===")
    print("1 - Cadastrar tarefa")
    print("2 - Ver tarefas")
    print("3 - Buscar tarefa")
    print("4 - Ver próxima tarefa")
    print("5 - Concluir tarefa")
    print("6 - Desfazer última ação")
    print("7 - Excluir tarefa")
    print("8 - Carregar arquivo")
    print("0 - Sair")


while True:

    mostrar_menu()

    opcao = input("Escolha: ")

    # 1
    if opcao == "1":

        titulo = input("Título: ")
        descricao = input("Descrição: ")
        disciplina = input("Disciplina: ")
        prazo = input("Prazo: ")

        tarefa = service.cadastrar_tarefa(
            titulo,
            descricao,
            disciplina,
            prazo
        )

        print("\nTarefa cadastrada com sucesso!")
        print(tarefa)

    # 2
    elif opcao == "2":

        tarefas = service.listar_tarefas()

        if len(tarefas) == 0:
            print("\nNenhuma tarefa cadastrada.")

        else:
            print("\n=== LISTA DE TAREFAS ===")

            for i, tarefa in enumerate(tarefas):
                print(f"[{i}] {tarefa}")

    # 3
    elif opcao == "3":

        titulo = input("Digite o título da tarefa: ")

        tarefa = service.buscar_tarefa(titulo)

        if tarefa:
            print("\nTarefa encontrada:")
            print(tarefa)

        else:
            print("\nTarefa não encontrada.")

    # 4
    elif opcao == "4":

        tarefa = service.proxima_tarefa()

        if tarefa:
            print("\nPróxima tarefa:")
            print(tarefa)

        else:
            print("\nFila vazia.")

    # 5
    elif opcao == "5":

        tarefa = service.concluir_tarefa()

        if tarefa:
            print("\nTarefa concluída:")
            print(tarefa)

        else:
            print("\nNenhuma tarefa pendente.")

    # 6
    elif opcao == "6":

        tarefa = service.desfazer_ultima_acao()

        if tarefa:
            print("\nAção desfeita:")
            print(tarefa)

        else:
            print("\nNenhuma ação para desfazer.")

    # 7
    elif opcao == "7":

        try:
            indice = int(input("Digite o índice da tarefa: "))

        except ValueError:
            print("\nDigite um número válido.")
            continue

        tarefa = service.excluir_tarefa(indice)

        if tarefa:
            print("\nTarefa removida:")
            print(tarefa)

        else:
            print("\nÍndice inválido.")

    # 8
    elif opcao == "8":

        sucesso = service.carregar_arquivo("data/tarefas.txt")

        if sucesso:
            print("\nArquivo carregado com sucesso!")

        else:
            print("\nErro ao carregar arquivo.")

    # 0
    elif opcao == "0":

        print("\nEncerrando sistema...")
        break

    else:
        print("\nOpção inválida.")