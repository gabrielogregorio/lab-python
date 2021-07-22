# metodo usado para pesquisa em classe
# para pesquisar o metodo correto em 
# classe que tem multipla herança

# Em multiplas heranças, qualquer elemento é
# buscado primeiro na classe que ele esta
# Depois nas superiores

class Veiculo():
	texto = 'Veiculo'

	def __init__(self):
		pass


class Trem(Veiculo):
	texto = 'Trem'
	pass

class Carro(Veiculo):
	#texto = 'Carro'
	def __init__():
		# O MRO é usado automaticamente
		super(Carro, self).__init__()

"""
USE COM MODERAÇÃO
"""
class CarroTrem(Carro, Trem):
	#texto = 'CarroTrem'
	pass

print(CarroTrem.__mro__)
print(CarroTrem.texto)

#print(CarroTrem.mro())
# Ordem de pesquisa
# De um atribuito
#1. <class '__main__.CarroTrem'> (1. Atual)
#2. <class '__main__.Carro'> (2. esqu)
#3. <class '__main__.Trem'> (3. direita)
#4. <class '__main__.Veiculo'> (4. Princ)
#5. <class 'object'>)

"""
quando você usa o super, o MRO é usado
Automaticamente
"""
