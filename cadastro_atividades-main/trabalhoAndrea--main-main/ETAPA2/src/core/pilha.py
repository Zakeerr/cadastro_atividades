class PilhaHistorico:
    def __init__(self):
        self.pilha = []

    def push(self, acao):
        self.pilha.append(acao)

    def pop(self):
        if self.esta_vazia():
            return None
        return self.pilha.pop()

    def peek(self):
        if self.esta_vazia():
            return None
        return self.pilha[-1]

    def esta_vazia(self):
        return len(self.pilha) == 0