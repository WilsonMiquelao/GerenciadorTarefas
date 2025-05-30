from models import tarefas
from controllers import ordenar_por_prioridade, agrupar_por_categoria

def mostrar_tarefas():
    i = 1
    for tarefa in tarefas:
        print(f"\nTarefa {i}:")
        for chave in tarefa:
            chave_formatada = chave[0].upper() + chave[1:]
            print(f"{chave_formatada}: {tarefa[chave]}")
        i += 1

def mostrar_por_prioridade():
    ordenar_por_prioridade()
    print("\nTarefas por Prioridade:")
    for tarefa in tarefas:
        print(f"- {tarefa['nome']} (Prioridade: {tarefa['prioridade']})")

def mostrar_por_categoria():
    categorias = agrupar_por_categoria()
    print("\nCategorias Disponíveis:")
    for cat in categorias:
        print(f"• {cat}")
    
    escolha = input("\nEscolha uma categoria: ")
    if escolha in categorias:
        print(f"\nTarefas em '{escolha}':")
        for t in categorias[escolha]:
            print(f"→ {t['nome']}: {t['descricao']}")
    else:
        print("Categoria não encontrada!")