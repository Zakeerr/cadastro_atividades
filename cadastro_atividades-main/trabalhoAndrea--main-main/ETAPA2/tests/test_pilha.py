import unittest

from src.core.pilha import PilhaHistorico


class TestPilha(unittest.TestCase):

    def setUp(self):
        self.pilha = PilhaHistorico()

    def test_push_pop(self):

        self.pilha.push("acao")

        resultado = self.pilha.pop()

        self.assertEqual(resultado, "acao")

    def test_pilha_vazia(self):

        self.assertIsNone(self.pilha.pop())

    def test_multiplos_elementos(self):

        self.pilha.push("A")
        self.pilha.push("B")

        self.assertEqual(self.pilha.pop(), "B")
        self.assertEqual(self.pilha.pop(), "A")


if __name__ == "__main__":
    unittest.main()