string = 'Isso é um texto'

# posição 0
print(string[0])

# Da posição 0 até a 2
print(string[0:2])

# Localize e filtre
print(string[ string.find('é')+2 : string.find('te')-1 ] )

# da posição inicial até a 10
print(string[:10])

# da posição 10 até a final
print(string[10:])

# de zero até o final de dois em dois
print(string[0:len(string):2])

# andando pelos caracteres da string
for caractere in string:
    # o end evita a quebra de linha
    print(caractere, end='')

print('')

# Andando de 0 a 9 e mostrando o valor do indice na string
for caractere in range(0,10):
    print(string[caractere], end='')
