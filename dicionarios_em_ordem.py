from collections import OrderedDict

# Deveria trazer os dicionários na ordem que foram inseridos
# mas no python3.8 isso parece que já acontece
# Estranho
d = OrderedDict()

d['php'] = 10
d['python'] = 10
d['Java'] = 3
d['C'] = 2

print(d)


d2 = {}
d2['php'] = 10
d2['python'] = 10
d2['Java'] = 3
d2['C'] = 2
print(d2)

