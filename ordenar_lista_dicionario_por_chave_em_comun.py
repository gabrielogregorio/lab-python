linha = [
    # MINUSCULAS E MAIUSCULAS
    # AFETAM A ORDENACAO
	{"nome":"gabriel"},
	{"nome":"marcos"},
	{"nome":"tarabela"},
	{"nome":"ana"},
	{"nome":"zeunalu"},
	{"nome":"xilena","idade":24}
]

from operator import itemgetter

# PODE ORDENAR POR MULTIPLAS CHAVES
linhas_pelo_nome = sorted(linha, key=itemgetter('nome'))
print(linhas_pelo_nome)