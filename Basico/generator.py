"""

iterador produzi itens iterando sobre outro objeto
gerador e um iteravel que produz itens sem necessariamente acessar outra colecao ele pode gferar itens sem dependencfia externa
uma funcao geradora possui a palavra yield

CALCULO SOBRE DEMANDA
!!!!!!!!!!INCRIVEL!!!!!!!!!!!!
"""

gen = (l for l in 'abc')

print(gen.__next__())
print(gen.__next__())
print(next(gen))


def fib(max):
    x, y = 1, 1
    while x < max:
        yield x
        x, y = y, x + y

# OBJETO ITERAVEL, POSSO FAZER UM FOR
gen = fib(1000000000000000000000000000000000000000000000000000000000000000000000000000000)

#for i in gen:
#    print(i)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Vai até onde precisa. UAL
