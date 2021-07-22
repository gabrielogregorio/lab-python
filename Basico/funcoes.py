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

# O X ESTA VINDO DE FORA DO PROGRAMA
x = 10
a = lambda y: x + y
print(a(10))

x = 40
print(a(10))

print()
# SE VOCE QUER TRAVA O X,
# DEIXE COMO DEFAULT
x = 10
a = lambda y, x=x: x + y
print(a(10))

x = 40
print(a(10))


#==========================#

# Uma tupla
def funcao(*args):
	return args

print(funcao([1, 2, 3, 4, 5]))

#==========================#

# e se os parametros forem nomeados
def funcao(**kwargs):
	return kwargs

print(funcao(
	idade=22,
	nome='gabriel'
	))
