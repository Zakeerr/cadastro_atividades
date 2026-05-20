import unittest

from src.core.lista import ListaTarefas
from src.core.tarefa import Tarefa


class TestLista(unittest.TestCase):

    def setUp(self):
        self.lista = ListaTarefas()

    def test_inserir_tarefa(self):

        tarefa = Tarefa(
            "Projeto",
            "Descricao",
            "ED",
            "20/05"
        )

        self.lista.inserir(tarefa)

        self.assertEqual(len(self.lista.tarefas), 1)

    def test_remover_tarefa(self):

        tarefa = Tarefa(
            "APS",
            "Descricao",
            "Banco",
            "25/05"
        )

        self.lista.inserir(tarefa)

        removida = self.lista.remover(0)

        self.assertEqual(removida, tarefa)

    def test_buscar_tarefa(self):

        tarefa = Tarefa(
            "Trabalho",
            "Descricao",
            "POO",
            "30/05"
        )

        self.lista.inserir(tarefa)

        resultado = self.lista.buscar("Trabalho")

        self.assertEqual(resultado, tarefa)


if __name__ == "__main__":
    unittest.main()