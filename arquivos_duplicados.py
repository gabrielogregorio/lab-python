from os import walk, path

# Coloque o diretório aqui
diretorio = '/home/gabriel/Área de Trabalho'

# Arquivos repetidos
dic_repetidos = {}

# Loop por todos os diretórios
for (dirpath, dirnames, filenames) in walk(diretorio):

    # Loop por todos os arquivos
    for file in range( len( filenames )):

        # Tente obter o tamanho do arquivo
        try:
            tam = str( path.getsize(dirpath + '/' + filenames[file]) )

        # Se der errado
        except:
            tam = '123456' + filenames[file]

        # Verifica se já existe no dicionário
        try:
            dic_repetidos[ tam + filenames[file]]

        # Adicione no dicionário
        except:
            dic_repetidos[ tam + filenames[file]] = [[dirpath + '/' + filenames[file]]]

        # Incremente no dicionario
        else:
            dic_repetidos[ tam + filenames[file]].append([dirpath + '/' + filenames[file]])

# Ande por todos os itens
for k, v in dic_repetidos.items():

    # Se tive mais de um valor
    if len( v ) > 1:

        # Ande por todos os valores de v
        for valores in v:

            # Mostre o valor
            print(valores)

        # Adicione uma linha em branco
        print('')