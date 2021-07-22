class Pessoa:
	__slots__ = ['nome', 'idade']
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

i = Pessoa('gabriel', 25)
i.nome

# Os slots fazem com que o python trate os argumentos de forma
# mais compacta economizando memória.
# O efeito colateral do slots é que não da para modificar os atributos
# e esse efeito colateral não pode ser considerado encapsulamento
