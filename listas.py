lista = [1,2,3,4,5,6,7]  # lista
print(lista)             # Exibindo a lista

lista.append(8)          # Adicionar item
print(lista)             # exibindo a lista

lista.pop()              # Remover o ultimo elemento
print(lista)             # exibindo a lista

print(lista[0:5])        # Fazendo slicing

print( len(lista) )      # Exibindo o tamanho da lista

lista[2] = 'texto'       # Mudando valores
print(lista)             # exibindo a lista

lista.insert(2, "Antes do texto") # Inserir em uma posição especifica
print(lista)                      # exibindo a lista
nova_lista = ['final','final+1']  # Adicionar nova lista
lista.extend(nova_lista)          # Extender lista
print(lista)                      # exibindo a lista

lista1 = ['gabriel','gregorio']
lista2 = ['da','silva']

print("gabriel" in lista1) # Tem Gabriel dentro da liista?
print("lua" in lista1)     # Tem lua na frase?

print(lista1)
print(lista2)

print( lista1 + lista2 )   # Concatenando duas listas
print(lista1*2)            # Multiplicar uma lista por 2
lista1.remove('gabriel')   # remover uma valor especifico
print(lista1)              # exibindo a lista novamente

# Lista de notas
notas = [9.87, 9.83, 6.65, 3.64, 7.76, 9.57, 9.07, 7.67, 8.45, 3.53, 2.42, 9.75, 9.78, 9.24, 8.53, 7.35, 2.34, 6.56, 8.67]

print(max(notas))       # Maior nota
print(min(notas))       # Menor nota

alunos = ['a','b']      # Lista

backup = alunos.copy()  # fazer uma copia da lista alunos
print(alunos)
print(backup)

alunos.clear()          # Limpar a lista alunos
print(alunos)
print(backup)

codigo = [0,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0] # CONTAGEM DE VALORES
print(codigo.count(1))

lista = ['b','a','c','e','d'] # lista original
print(lista)

lista.sort()            # Ordenar lista
print(lista)

lista.reverse()         # Reverter a ordem atual
print(lista)
