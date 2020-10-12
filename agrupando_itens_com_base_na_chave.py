from operator import itemgetter
from itertools import groupby

exemplos = [
	('marcos', 20),
	('zeues', 23),
	('marcos', 24),
	('jose', 38)
]


# Ordenar pelo nome
exemplos.sort(key=itemgetter(0))
print(exemplos)


print({key:
	# Retornar os valores em ordem crescente
	sorted(
		# Especificar qual é o valor
		# Retorna uma nova lista com um score unico
		map(itemgetter(1), value))
			for key, value in groupby(exemplos, key=itemgetter(0)) })