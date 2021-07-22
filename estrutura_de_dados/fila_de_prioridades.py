import heapq


class FilaDePrioridade:
	def __init__(self):
		self.fila = []
		self.indice = 0

	def push(self, item, prioridade):
		heapq.heappush(self.fila, (
			-prioridade,
			self.indice,
			item))

	def pop(self):
		return heapq.heappop(self.fila)[-1]


class Item:
	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

fila = FilaDePrioridade()

# Item e prioridade(idade neste caso)
fila.push(Item('Gabriel'), 22)
fila.push(Item('João'), 78)
fila.push(Item('Marcos'), 65)
fila.push(Item('Maria'), 20)

print(fila.pop())
print(fila.pop())
print(fila.pop())
print(fila.pop())
