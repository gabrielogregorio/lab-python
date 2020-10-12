print((1).__add__(2))
# =============== #
print(1 + 2)
# =============== #

class MeuInt(int):
	def __add__(self, num):
		return 0
a = MeuInt(1)
print(a + 2)




class ListaPersonalizada(list):
	def append(self, *args):
		self.extend(args)

lista = ['gabriel', 'lucian', 'james', 'carlos']
print(lista)

lista2 = ListaPersonalizada()
lista2.append(1)#, 'lucian', 'james', 'carlos')
lista2.append(1, 3, 5, 6, 7)#, 'lucian', 'james', 'carlos')

print(lista2)




class ListaPersonalizada(list):
	def sort(self):
		return 'Não quero ordenar hoje'


lista = ['gabriel', 'lucian', 'james', 'carlos']
lista.sort()
print(lista)

lista2 = ListaPersonalizada()
print(lista2.sort())
