lista = [1, 2, 3]

import time

inicio = time.time()
for i in lista:
	print(i, end='')
fim = time.time()
print(fim-inicio)
print()

# ========================== #

inicio = time.time()
for i in reversed(lista):
	print(i, end='')
fim = time.time()
print(fim-inicio)
