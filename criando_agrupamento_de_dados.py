linhas = [
	{"nome":"abc", "data":"15/01/2020"},
	{"nome":"def", "data":"31/11/2020"},
	{"nome":"zzz", "data":"20/10/2020"},
	{"nome":"fff", "data":"15/01/2020"},
	{"nome":"ggg", "data":"31/11/2020"}
]

from operator import itemgetter
from itertools import groupby

# Ordenar as datas
linhas.sort(key=itemgetter('data'))

# Agrupar as datas, !!!!!!!!ANTES DE AGRUPAR, ORDENE!!!!!
for data, items in groupby(linhas, key=itemgetter('data')):
	print(data)
	for i in items:
		print('   ', i)

