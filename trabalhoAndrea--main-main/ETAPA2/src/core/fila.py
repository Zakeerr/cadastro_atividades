class FilaPendencias:
    def __init__(self):
        self.fila = []

    def enqueue(self, tarefa):
        self.fila.append(tarefa)

    def dequeue(self):
        if self.esta_vazia():
            return None
        return self.fila.pop(0)

    def peek(self):
        if self.esta_vazia():
            return None
        return self.fila[0]

    def esta_vazia(self):
        return len(self.fila) == 0

    def exibir(self):
        return self.fila