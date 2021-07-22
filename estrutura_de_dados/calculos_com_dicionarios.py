d = {
		'tablet': 2000,
		'notebook': 5850,
		'iphone': 5000
    }

print(d)
# O ZIP SÓ PODE SER CONSUMIDO UMA VEZ

menor_preco = min(zip(d.values(), d.keys()))
print(menor_preco)

maior_preco = max(zip(d.values(), d.keys()))
print(maior_preco)
