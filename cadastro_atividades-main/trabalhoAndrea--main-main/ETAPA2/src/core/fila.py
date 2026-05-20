from collections import deque


class FilaPendencias:
    def __init__(self):
        self.fila = deque()

    def enqueue(self, tarefa):
        self.fila.append(tarefa)

    def dequeue(self):
        if self.esta_vazia():
            return None

        return self.fila.popleft()

    def peek(self):
        if self.esta_vazia():
            return None

        return self.fila[0]

    def esta_vazia(self):
        return len(self.fila) == 0

    def exibir(self):
        return list(self.fila)