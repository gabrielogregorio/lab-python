# Encapsulamento de código.
# Restringir o aceso a atributos e métodos
# Atributos publico e privado
class P():
	def __init__(self, x):
		self.x = x

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		if (x > 0):
			self._x = x
		else:
			raise 'Você precisa definir um valod válido'
	

p = P(10)
print(p.x)
p.x = -100
print(p.x)