a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

# Como executar pesquisa em ambos os dicionários?
from collections import ChainMap
c = ChainMap(a, b)

print(c['x'])
print(c['y'])
# SE TIVERMOS CHAVES DUPLICADAS
# A CHAVE DO PRIMEIRO MAPEAMENTO
# SERA USADA
print(c['z'])

print(len(c))
#del c['x']
print()
merged = dict(b)
merged.update(a)
merged['x']
merged['y']
merged['z']
print(a)
print(b)
print(merged)


