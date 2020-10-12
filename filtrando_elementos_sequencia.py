import math

lista = [10, -5, -10, 20, 25, 30, 50, -100]
print([math.sqrt(i) for i in lista if i > 0])
print([i for i in lista if i <= 0])

# Como pode gerar um valor grande,
# podemos usar um generator
gen = (i for i in lista if i <= 0)
for j in gen:
	print(j)

