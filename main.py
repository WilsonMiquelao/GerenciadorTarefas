from controllers import adicionar_tarefa, marcar_como_concluida
from views import mostrar_tarefas, mostrar_por_prioridade, mostrar_por_categoria

def menu():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Ver por Prioridade")
        print("5. Ver por Categoria")
        print("6. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            desc = input("Descrição: ")
            prio = int(input("Prioridade (1-5): "))
            cat = input("Categoria: ")
            adicionar_tarefa(nome, desc, prio, cat)
            print("Tarefa adicionada!")

        elif opcao == "2":
            mostrar_tarefas()

        elif opcao == "3":
            num = int(input("Número da tarefa: "))
            print(marcar_como_concluida(num))

        elif opcao == "4":
            mostrar_por_prioridade()

        elif opcao == "5":
            mostrar_por_categoria()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()