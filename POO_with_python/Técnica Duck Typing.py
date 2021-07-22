# Técnica Duck Typing. Se um objeto anda como um pato e faz quack como um pato então ele é um pato!

# Funciona com qualquer linguagem OO.
# Um objeto responde a uma mensagem caracteristica, então ele é do mesmo tipo.

'''
caminhao = Caminhao()
carro = Carro()

Ambos respondem ao método .acelerar()
caminhao.acelerar()
carro.acelerar()

'''

class Livro():
    def __init__(self, titulo, lancamento, autor):
        self.titulo = titulo
        self.lancamento = lancamento
        self.autor = autor
    def falar(self):
        print('livro')

class Filme():
    def __init__(self, titulo, lancamento, diretor):
        self.titulo = titulo
        self.lancamento = lancamento
        self.diretor = diretor
    def falar(self):
        print('filme')

# Isso é duck typing
def imprimir(midia):
    print(midia.titulo, midia.lancamento)

machado = Livro('Os três aviões', 1922, 'Machado da Silva')
king_kong = Filme('Os pilotos', 2055, 'Rainouds Sturards')

imprimir(machado)
imprimir(king_kong)


'''
Se ele faz quack, ele é um pato. Não importa mais nada.
Programe para interfaces e não para implementação.

Você não deve verificar se ele é um pato, mas sim se ele
age como um pato!
'''

##################
# VERSAO 2.0 do imprimir

def imprimir2(obj):
    # Verifica se é um pato de verdade...........
    # ISSO NÂO É PYTHONICO, NAO É DUCKTYPING!!
    # NÃO NÃO NÃO NÃO NÃO NÃO NÃO NÃO NÃO NÃO NÃO NÃO
    if isinstance(obj, Filme):
        print(obj.titulo, obj.lancamento)
    else:
        print('Precisa ser um filme!')

imprimir2(machado)
imprimir2(king_kong)
## VERSAO 3

def imprimir3(obj):
    # TAMBÈM NAO É PYTHONICO!
    if hasattr(obj, 'falar'):
        if callable(obj.falar):
            print(obj.falar())

imprimir3(machado)
imprimir3(king_kong)

# VERSAO 4, QUAL É O MLEHOR? EAFP é A RESPOSTA. PYTHONICO
# EASP você TENTA. LBYL você testa e depois executa
# ISSO É PYTHONICO
def imprimir4(obj):
    try:
        obj.falar()
    except AttributeError as e:
        print(e)

import re
imprimir4(machado)
imprimir4(re)
