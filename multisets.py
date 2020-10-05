# multiset
'''
{a, a, a, b, b}
a tem multiplicidade 3
b tem multiplicidade 2
'''

from collections import Counter

# multiplicidade
c = Counter(a=3, b=2, c=1)
print(list(c.elements()))

print("2 elementos mais comuns")
print(c.most_common(2))