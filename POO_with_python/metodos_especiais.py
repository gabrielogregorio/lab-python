class Complex:
	# METODOS ESPECIAIS
	#__init__
	#__repr__
	#__add__
	#__sub__
	#__len__
	#__new__
	#__get__
	# e muito mais

	def __init__(self, r, i):
		self.r = r
		self.i = i

	def __repr__(self):
		return '{0}, {1}i'.format(self.r, self.i)

    # é o +
	def __add__(self, other):
		return Complex(self.r + other.r, self.i + other.i)

    # é o -
	def __sub__(self, other):
		return Complex(self.r - other.r, self.i - other.i)


c1 = Complex(3, 2)
c2 = Complex(2, 3)
c3 = c1 - c2
print(c3)
