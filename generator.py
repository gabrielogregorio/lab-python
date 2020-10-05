gen = (l for l in 'abc')

print(gen.__next__())
print(gen.__next__())
print(next(gen))
