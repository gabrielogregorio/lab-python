# funções normais
def soma(valor1,valor2):
    return valor1+valor2

# entrada de dados
valor1 = 5
valor2 = 4

print('A soma de {} com {} é {}'.format(valor1,valor2, soma(valor1,valor2)))


# funções lambda
x = 10
y = 20
soma_l = lambda x,y: x+y

print("A soma de {} e {} é {}".format(x, y , soma_l(x,y)))