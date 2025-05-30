# ✅ Gerenciador de Tarefas em Python

Visão Geral do Projeto
Este é um gerenciador de tarefas simples em Python que utiliza uma arquitetura MVC (Model-View-Controller) para organizar o código. O programa permite adicionar, visualizar e gerenciar tarefas com diferentes prioridades e categorias.

Lógica e Estrutura do Código
Arquitetura MVC
O projeto está organizado em três componentes principais:

Model (model.py): Gerencia a estrutura de dados e o "banco de dados" das tarefas

Mantém a lista global tarefas

Define a função nova_tarefa() que cria a estrutura padrão de uma tarefa

View (view.py): Responsável por toda a exibição/interação com o usuário

Mostra listagens de tarefas de diferentes formas

Formata a saída para o usuário

Controller (controller.py): Contém a lógica de negócios e manipulação dos dados

Implementa as operações CRUD (Create, Read, Update, Delete)

Ordena e agrupa tarefas conforme necessário

Fluxo do Programa (main.py)
O arquivo principal implementa um loop de menu que:

Exibe opções para o usuário

Coleta a entrada do usuário

Chama as funções apropriadas nos controllers e views

Mantém o programa em execução até que o usuário escolha sair

Lógicas Implementadas
Adição de Tarefas:

Coleta dados do usuário (nome, descrição, prioridade, categoria)

Cria um novo dicionário representando a tarefa

Adiciona à lista global de tarefas

Listagem de Tarefas:

Mostra todas as tarefas com seus detalhes completos

Numera as tarefas para referência posterior

Marcação como Concluída:

Implementa uma lógica dupla:

Se a tarefa não estava concluída, marca como concluída

Se já estava concluída, remove a tarefa da lista

Verifica limites do array para evitar erros

Ordenação por Prioridade:

Implementa um algoritmo de ordenação (bubble sort)

Organiza as tarefas da maior para a menor prioridade

Agrupamento por Categoria:

Cria um dicionário onde as chaves são categorias

Cada categoria contém uma lista de tarefas correspondentes

Permite visualização seletiva por categoria escolhida
