class Pessoa:
    # especificador
    # NÃO SERÁ MAIS POSSIVEL ADICIONAR ATRIBUTOS
    # SLOTS NÃO É UMA FERRAMENTA DE ENCAPSULAMENTO, ACABA
    # SENDO UM EFEITO COLATERAL, MAS NÃO É O PROPÒSITO
	__slots__ = ['nome', 'idade', 'peso']
	def __init__(self, nome, idade, peso):
		self.nome = nome
		self.idade = idade
		self.peso = peso

		# Usando o slots, o python
		# não colocará os atributos
		# em um dicionário, mas sim
		# em um array, muito semelhante
		# a uma lista ou tupla