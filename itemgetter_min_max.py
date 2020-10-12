from operator import itemgetter

dados = [
	{
		"nome":"gabriel",
		"idade":22
	},
	{
		"nome":"Carla",
		"idade":27
	},
]

print(min(dados, key=itemgetter('nome')))
print(max(dados, key=itemgetter('nome')))
print()
print(min(dados, key=itemgetter('idade')))
print(max(dados, key=itemgetter('idade')))
