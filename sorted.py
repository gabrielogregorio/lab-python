lista = [6, 3, 7, 2, 4, 3]
tupla = (8, 2, 5, 4, 1, 3)
dicio = {9:'a', 3:'f', 7:'b'}

print()
print(lista)
print(sorted(lista))
print()
print(tupla)
print(sorted(tupla))
print()
print(dicio)
print(sorted(dicio))


class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def __repr__(self):
		return self.nome

p1 = Pessoa('Gabriel', 21)
p2 = Pessoa('Maria', 23)
p3 = Pessoa('Ana', 46)
p4 = Pessoa('Cristina', 32)

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.nome))
print(sorted(pessoas, key=lambda pessoa: pessoa.idade))

