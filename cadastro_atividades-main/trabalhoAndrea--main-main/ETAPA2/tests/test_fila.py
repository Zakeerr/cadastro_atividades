import unittest

from src.core.fila import FilaPendencias
from src.core.tarefa import Tarefa


class TestFila(unittest.TestCase):

    def setUp(self):
        self.fila = FilaPendencias()

    def test_enqueue_dequeue(self):

        tarefa = Tarefa(
            "Fila",
            "Descricao",
            "ED",
            "10/05"
        )

        self.fila.enqueue(tarefa)

        removida = self.fila.dequeue()

        self.assertEqual(removida, tarefa)

    def test_fila_vazia(self):

        self.assertIsNone(self.fila.dequeue())

    def test_multiplos_elementos(self):

        tarefa1 = Tarefa("A", "D", "ED", "01")
        tarefa2 = Tarefa("B", "D", "ED", "02")

        self.fila.enqueue(tarefa1)
        self.fila.enqueue(tarefa2)

        self.assertEqual(self.fila.dequeue(), tarefa1)
        self.assertEqual(self.fila.dequeue(), tarefa2)


if __name__ == "__main__":
    unittest.main()