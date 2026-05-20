from src.core.fila import FilaPendencias

fila = FilaPendencias()

fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C")

print("Fila atual:", fila.fila)

print("Removido:", fila.dequeue())

print("Fila depois:", fila.fila)