class Classe(object):
   pass

# TOdas as classes herdam implicitamente de object

#----------------

#class Funcionario:#
#	def get_teste(self):#
#		return 10


#class Gerente(Funcionario):#
#	def __init__(self):
#		pass

#	def get_teste(self):#
#		return super().get_teste() + 1000

#g = Gerente()
#print(g.get_teste())
# SUper chama métodos e atributos da classe super


#------------
# Outra forma

class Funcionario:
	def __init__(self, nome, salario):
		self.nome = nome
		self.salario = salario

	def get_teste(self):
		return 10


class Gerente(Funcionario):
	def __init__(self, nome, salario, bonus):
		super().__init__(nome, salario)
		self.bonus = bonus

	def get_teste(self):
		return super().get_teste() + 1000

g = Gerente('Gabriel', 18921.00, 300)
print(g.get_teste())
print(g.bonus)
