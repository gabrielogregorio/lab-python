import itertools

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = ['a', 'b', 'c']

soma = itertools.chain(l1, l2, l3)
print(list(soma))