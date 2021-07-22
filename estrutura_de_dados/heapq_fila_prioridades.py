import heapq

idades = [10, 14, 16, 20, 12, 21]
print(idades)

print(heapq.nsmallest(3, idades))
print(heapq.nsmallest(2, idades))
print(heapq.nsmallest(1, idades))

print(heapq.nlargest(3, idades))
print(heapq.nlargest(2, idades))
print(heapq.nlargest(1, idades))


# Fila no formato heapify
print(heapq.heapify(idades))

