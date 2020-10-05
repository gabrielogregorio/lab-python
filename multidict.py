from collections import defaultdict

d = defaultdict(list)

d['gabriel'].append(20)
d['gabriel'].append(23)
d['gabriel'].append(26)
d['gabriel'].append(28)
d['gabriel'].append(28)

print(d['gabriel'])
# [20, 23, 26, 28, 32]


# ------------
# Sem elementos repetidos
d2 = defaultdict(set)
d2['gabriel'].add(20)
d2['gabriel'].add(23)
d2['gabriel'].add(23)
print(d2['gabriel'])
