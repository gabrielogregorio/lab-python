# Retorna um gerador
def gen():
    for i in range(10):
        yield i
        print('DATA')
# Ele congela
g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
