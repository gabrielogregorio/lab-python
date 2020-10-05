def pai(num):
	def filho1():
		print('sou o filho 1')

	def filho2():
		print("sou o filho 2")

	try:
		assert num == 10
		return filho1
	except AssertionError:
		return filho2


f1 = pai(10)
f2 = pai(20)

f1()
f2()