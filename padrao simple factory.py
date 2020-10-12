from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	@abstractmethod
	def som(self):
		pass

class Cachorro(Animal):
	def som(self):
		print("au au")

class Gato(Animal):
	def som(self):
		print("miau miau")


class Coelho(Animal):
	def som(self):
		print("Grishi")
'''
nina = Gato('Nina', 4)
rex = Cachorro('Rex', 6)
jose = Coelho('jose', 1)
rex.som()
nina.som()
jose.som()
'''

class Fabrica(object):
	def produzir_som(self, object_type, nome, idade):
		return eval(object_type)(nome, idade).som()

f = Fabrica()

f.produzir_som('Gato', 'Nina', 2)
f.produzir_som('Cachorro', 'Rex', 6)
f.produzir_som('Coelho', 'jose', 1)
