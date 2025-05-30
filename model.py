# Lista principal de tarefas (nosso "banco de dados")
tarefas = []

# Estrutura/modelo de uma tarefa
def nova_tarefa(nome, descricao, prioridade, categoria):
    return {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }