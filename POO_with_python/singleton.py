# Padrão de projeto

class Singleton(object):
	# Método __new__ instancia objetos, vamos sobrescreve-lo
	def __new__(cls):
		# Se a classe tem a instancia, então aloca o objeto existente
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance
'''
class Singleton():
	def __init__(cls):
		pass
'''

s1 = Singleton()
s2 = Singleton()
s3 = Singleton()
s4 = Singleton()


print(s1)
print(s2)
print(s3)
print(s4)



'''
NORMAL
$=========================================================$
$    0x7f4533dfb1c0     0x7f4533d0ae50     0x7f4533d0a310 $
$    0x7f4533d15fa0                                       $
$=========================================================$

SINGLETON
$=========================================================$
$    0x7fa056b09e50                                       $
$                                                         $
$=========================================================$
'''