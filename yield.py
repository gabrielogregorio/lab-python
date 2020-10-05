# Retorna um gerador
def gen():
    yield 'top'

    for i in range(10):
        yield i

g = gen()
print(next(g))
print(next(g))
print(next(g))
