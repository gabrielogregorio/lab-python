class Objeto:
	def __init__(self, obj_id):
		self.obj_id = obj_id

    # Classe de representação
	def __repr__(self):
		return str(self.obj_id)

objetos = [Objeto(1), Objeto(2), Objeto(4), Objeto(3)]
from operator import attrgetter

print(objetos)

print(sorted(objetos, key=lambda obj: obj.obj_id))

# Normalmente é mais rápido
# Você pode usar multiplas chaves
print(sorted(objetos, key=attrgetter('obj_id')))
