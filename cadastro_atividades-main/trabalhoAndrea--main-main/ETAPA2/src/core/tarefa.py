class Tarefa:
    def __init__(self, titulo, descricao, disciplina, prazo):
        self.titulo = titulo
        self.descricao = descricao
        self.disciplina = disciplina
        self.prazo = prazo
        self.status = "Pendente"

    def concluir(self):
        self.status = "Concluída"

    def restaurar(self):
        self.status = "Pendente"

    def __str__(self):
        return f"{self.titulo} | {self.disciplina} | {self.prazo} | {self.status}"