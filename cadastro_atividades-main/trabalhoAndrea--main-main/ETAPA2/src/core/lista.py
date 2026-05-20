class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def inserir(self, tarefa):
        self.tarefas.append(tarefa)

    def remover(self, indice):
        if 0 <= indice < len(self.tarefas):
            return self.tarefas.pop(indice)
        return None

    def buscar(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo.lower() == titulo.lower():
                return tarefa
        return None

    def exibir(self):
        return self.tarefas