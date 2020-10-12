# Compreensao de dicionarios

precos = {
	"iphone":6700,
	"notebook":4100,
	"microsd":35,
	"netflix":40
}

somente_maior_que_100 = {
	key:value for key, value in precos.items()
		if value > 100}

print(somente_maior_que_100)