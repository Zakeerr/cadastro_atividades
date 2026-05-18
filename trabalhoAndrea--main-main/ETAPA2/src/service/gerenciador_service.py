from src.core.lista import ListaTarefas
from src.core.fila import FilaPendencias
from src.core.pilha import PilhaHistorico
from src.core.tarefa import Tarefa
from src.database.tarefa_repository import TarefaRepository


class GerenciadorService:

    def __init__(self):
        self.lista = ListaTarefas()
        self.fila = FilaPendencias()
        self.pilha = PilhaHistorico()
        self.repository = TarefaRepository()

    # 1
    def cadastrar_tarefa(self, titulo, descricao, disciplina, prazo):

        tarefa = Tarefa(
            titulo,
            descricao,
            disciplina,
            prazo
        )

        self.lista.inserir(tarefa)
        self.fila.enqueue(tarefa)

        try:
            self.repository.salvar(tarefa)
        except:
            pass

        return tarefa

    # 2
    def listar_tarefas(self):
        return self.lista.exibir()

    # 3
    def buscar_tarefa(self, titulo):
        return self.lista.buscar(titulo)

    # 4
    def proxima_tarefa(self):

        if self.fila.esta_vazia():
            return None

        return self.fila.peek()

    # 5
    def concluir_tarefa(self):

        tarefa = self.fila.dequeue()

        if tarefa is None:
            return None

        tarefa.concluir()

        self.pilha.push(tarefa)

        return tarefa

    # 6
    def desfazer_ultima_acao(self):

        tarefa = self.pilha.pop()

        if tarefa is None:
            return None

        tarefa.restaurar()

        self.fila.enqueue(tarefa)

        return tarefa

    # 7
    def excluir_tarefa(self, indice):

        tarefa = self.lista.remover(indice)

        if tarefa is None:
            return None

        # remove da fila também
        if tarefa in self.fila.fila:
            self.fila.fila.remove(tarefa)

        return tarefa

    # 8
    def carregar_arquivo(self, caminho):

        try:

            with open(caminho, "r", encoding="utf-8") as arquivo:

                for linha in arquivo:

                    dados = linha.strip().split(";")

                    if len(dados) == 4:

                        titulo, descricao, disciplina, prazo = dados

                        # evita duplicar tarefa
                        tarefa_existente = self.buscar_tarefa(titulo)

                        if tarefa_existente is None:

                            self.cadastrar_tarefa(
                                titulo,
                                descricao,
                                disciplina,
                                prazo
                            )

            return True

        except FileNotFoundError:
            return False