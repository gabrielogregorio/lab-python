class NumerosPares(list):
	def append(self, inteiro: int) -> None:
		if not isinstance(inteiro, int):
			raise TypeError('Somente números inteiros')


		if inteiro % 2:
			raise ValueError('Somente números pares')


		super().append(inteiro)
'''
instancia = NumerosPares()
instancia.append(2)
instancia.append(4)
instancia.append(6)
instancia.append(10)
instancia.append(100)

print(sum(instancia))
'''

dicionario = dict()
dicionario['Abacaxi'] = 10
dicionario['Melão'] = 20


print(dicionario.items())


class DicionarioPersonalizado(dict):
	def items(self):
		return 'MODIFICADO!'

dicionario2 = DicionarioPersonalizado()
dicionario2['Abacaxi'] = 10
dicionario2['Melão'] = 20
print(dicionario2.items())
