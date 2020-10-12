from collections import Counter

a = Counter([1, 2, 1, 2, 3, 4])
b = Counter([1, 1, 1, 2, 2, 3 ])

print(a)
print(b)

c = a + b
print(c)