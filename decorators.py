'''
é um design pattern
padrão de projeto de software que permite adicionar
um comportamento a um objetyo ja existente em tempo de execucoa
ele agrega dinamizamenet responsabilidades adicionais a um objeto
é uma funcao que recebe uma funcao como parametro, gera uma nova funcao que
adiciona algumas funcionalidades a funcao original e retorna a nova função
'''
'''
class paramaiusculo(object):
    # Instância passando a função
    def __init__(self,funcao):
        pass

    # passando argumentos da função quando ela for chamada
    def __call__(self,*argumentos):
        return argumentos[0].upper()

# Muda o comportamento da função
@paramaiusculo
def mostrar(nome):
    return nome

print(mostrar("Mariana"))


# ======================= #
print()
print()
# ======================= #

def modificar(funcao):
    def subtrair(a, b):
        return a-b
    return subtrair

@modificar
def soma(a, b):
    return a + b

print(soma(2, 3))

'''

'''
# Só vai somar se os dois forem pares
def modificar(funcao):
    def soma_pares(a, b):
        if a % 2 == 0 and b % 2 == 0:
            return a + b
        return a - b
    return soma_pares

@modificar
def soma(a, b):
    return a + b

print(soma(2, 4))
'''

def meu_decorador(funcao):
    acao = None
    def imprimir(a):
        return "Mais aleatório impossivel"
    return imprimir
    return funcao

@meu_decorador
def imprime(a):
    return "RODOU A FUNCAO"

""" O PYTHON FAZ ISSO
imprime = meu_decorador(imprime)
"""

print(imprime('olá amigo'))
print(imprime('ignorar'))
