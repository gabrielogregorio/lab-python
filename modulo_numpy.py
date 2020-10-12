# Pacote para computação ciêntifica
# Principalmente para trabalhar
# Com muitos dados

import numpy as np

# MUITO MAIS EFICIENTE QUE A LISTA
# PADRAO


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x, '+', y, '=', x + y)
print(x, '*', y, '=', x * y)

print("\nRAIZ QUADRADA DA LISTA")
print(np.sqrt(x))

print('\nMATRIX')
mat = np.matrix([[1,2], [3, 4]])
print(mat)

print("\nTRANSPOSTA")
print(mat.T)

print("\nINVERSA")
print(mat.I)