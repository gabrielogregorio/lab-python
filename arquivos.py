# criar um arquivo
file = open('arquivo.txt','w')
file.write('texto')
file.close

# abrir arquivo
file = open('arquivo.txt','r')
texto = file.read()
file.close()

print(texto)
