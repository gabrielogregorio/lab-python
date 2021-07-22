from itertools import compress

nomes = ['marcos', 'joao', 'maria', 'pedro']
count = [3, 2, 1, 4]

maior2 = [i>2 for i in count]
print(maior2)

# Retornar de acordo com outra 
# lista com os valores que correspondem
print(list(
	# Retorna um iterator
	compress(nomes, maior2)))