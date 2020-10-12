a = {"a":1, "b":2, "c":3}
b = {"b":4, "c":5, "d":6}

print(a.keys() & b.keys())
# {'c', 'b'}

print(a.keys() - b.keys())
# {'a'}
# Está em a, mas não está em b

print(b.keys() - a.keys())
# {'d'}
# Está em a, mas não está em b

# Pode ter problemas com valores