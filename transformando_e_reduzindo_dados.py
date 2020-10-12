lista = [10, 5, 2, 3, 1, 5]
# Funçõo de redução
print(sum(lista))
print(max(lista))
print(min(lista))
print()
import time

start = time.time()
# Soma dos quadrados
soma_quad = sum([x * x for x in lista])
print(soma_quad)
print(start - time.time())

# Como deixar mais ediciente?
# Usando um argumento que corresponde a uma expressão geradora
start = time.time()
soma_quad = sum(x * x for x in lista)
print(soma_quad)
print(start - time.time())

