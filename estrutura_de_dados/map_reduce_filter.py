from functools import reduce
# ============================ MAP ============================ 
# temperaturas em graus célsius
celsius = [23,25,26,27,37,36,25,24,36,35,36,25,24,23,25]

# converter para graus fahrenheit
fahrenheit = list(map(lambda c:((c*9)/5)+32,celsius))

print(celsius)
print(fahrenheit)

# ============================ REDUCE ============================ 
# elementos
elementos = [10,35,34,25,16,17]

# somatório dos elementos
soma = int(reduce(lambda x , y: x + y , elementos))
print(elementos)
print(soma)

# ============================ FILTER ============================
resultados = [5,7,3,5.2,6,3,7,8,3,9,3,6.8,8,4,8,9,5,3,6,2,6,3,8.3,4,6,9.2,5,6,3,9.5]
filtro = list(filter(lambda x : x > 8 , resultados))

print(resultados)
print(filtro)