from models import tarefas, nova_tarefa

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = nova_tarefa(nome, descricao, prioridade, categoria)
    tarefas.append(tarefa)

def marcar_como_concluida(numero_tarefa):
    indice = numero_tarefa - 1
    if 0 <= indice < len(tarefas):
        if not tarefas[indice]["concluida"]:
            tarefas[indice]["concluida"] = True
            return f"Tarefa {numero_tarefa} marcada como concluída."
        else:
            tarefas.pop(indice)
            return f"Tarefa {numero_tarefa} removida."
    return "Número inválido."

def ordenar_por_prioridade():
    for i in range(len(tarefas)):
        for j in range(i+1, len(tarefas)):
            if tarefas[i]["prioridade"] < tarefas[j]["prioridade"]:
                tarefas[i], tarefas[j] = tarefas[j], tarefas[i]
    return tarefas

def agrupar_por_categoria():
    categorias = {}
    for tarefa in tarefas:
        cat = tarefa["categoria"]
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(tarefa)
    return categorias