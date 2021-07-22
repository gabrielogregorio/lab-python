class P:
	def __init__(self, x):
		self.__x = x

obj = P(10)
print(dir(obj))
print(obj._P__x)
obj._P__x = 20
print(obj._P__x)

# É MUITO RARO USAR ATRIBUTO PROTEGIDO,
# NORMALMENTE EM API, O RESTO VOCE USA ENCAPSULAMENTO
