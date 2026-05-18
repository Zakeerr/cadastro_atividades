import unittest

from src.core.fila import FilaPendencias
from src.core.pilha import PilhaHistorico
from src.core.lista import ListaTarefas
from src.core.tarefa import Tarefa


class TestSistema(unittest.TestCase):

    def test_fila(self):

        fila = FilaPendencias()

        tarefa = Tarefa(
            "Teste",
            "Descricao",
            "ED",
            "10/05"
        )

        fila.enqueue(tarefa)

        self.assertEqual(fila.peek(), tarefa)

    def test_pilha_vazia(self):

        pilha = PilhaHistorico()

        self.assertIsNone(pilha.pop())

    def test_lista_busca(self):

        lista = ListaTarefas()

        tarefa = Tarefa(
            "Projeto",
            "Descricao",
            "POO",
            "20/05"
        )

        lista.inserir(tarefa)

        resultado = lista.buscar("Projeto")

        self.assertEqual(resultado, tarefa)


if __name__ == "__main__":
    unittest.main()