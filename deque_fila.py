from collections import deque

'''
deque é uma extrutura de duas pontas
você pode remover do começo ou do inicio
é basicamente um fila, primeioro que entra
primeiro que sai. quem entra depois entra no
final
'''

# Maximo 3 elementos
fila = deque(maxlen=3)

# Entrando na fila
fila.append(1)
fila.append(2)
fila.append(3)
print(fila)

# Remoção do mais antigo da fila
fila.append(4)
print(fila)


# adição a direita e a esquerda
fila.appendleft('INICIO')
print(fila)

# Removendo do final
fila.pop()
print(fila)
fila.pop

# Adicionando no final
fila.append('FINAL')
print(fila)

# Removendo do inicio
fila.popleft()
print(fila)
