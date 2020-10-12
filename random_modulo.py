import random

lista = [1, 2, 3, 4, 5, 6]
print("UM NUMERO ALEATORIO DA LISTA")
print(random.choice(lista))

print("\nTRES VALORES ALEATORIO DIFERENTES")
print(random.sample(lista, 3))


print("\nFLOAT ENTRE 0 e 1")
print(random.random())

print("\nORDENAR LISTA DE FORMA ALEATORIA")
random.shuffle(lista)
print(lista)

print("\nALEATORIO, INTEIRO, ENTRE")
print(random.randint(0, 10))
