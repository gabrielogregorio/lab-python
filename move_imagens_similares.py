from PIL import Image
import imagehash
import shutil
import os


global movidos
movidos = []


def load_hashs(dir_base):
    print('carregando hash: {}'.format(dir_base))

    # Carrega um hash de todas as imagens
    dict_hashs = {}
    for file_1 in os.listdir(dir_base):

        # Tentar obter um hash de uma imagem
        try:

            # Formata o link
            arquivo_1 = os.path.join(dir_base, file_1)

            # Obtém o hash
            hash_1 = imagehash.average_hash(Image.open(arquivo_1))

            # adiciona no dicioário
            dict_hashs[file_1] = hash_1

        except Exception as erro:
            print(erro)

    return dict_hashs


def move_similar(dir_base):
    global movidos

    """
        Move todos os arquivos similares
        com menor tamaho para a pasta similar
    """

    # Carrega os hash
    dict_hashs = load_hashs(dir_base)

    # diretório para mover os arquivos similares
    ir_para = dir_base +'/similar/'

    # Anda por todos os arquivos
    for file_1, hash_1 in dict_hashs.items():

        # Ada pelos arquivos novamente
        for file_2, hash_2 in dict_hashs.items():

            # Se for o mesmo arquivo
            if file_2 == file_1:
                continue

            # Tenta obter o tamanho e mover os arquivos
            try:
                # Se a diferença entre os hash for pequena
                if hash_1 - hash_2 < 3:

                    # Obtem o tamanho dos dois arquivos
                    f1 = os.path.getsize(os.path.join(dir_base, file_1))
                    f2 = os.path.getsize(os.path.join(dir_base, file_2))

                    print('Tamanhos {} == {}'.format(file_1, file_2))

                    # Move o menor arquivo
                    if f1 > f2:
                        file = os.path.join(dir_base, file_2)

                        if file not in movidos:
                            shutil.move(file, ir_para)
                            movidos.append(file)

                    else:
                        file = os.path.join(dir_base, file_1)

                        if file not in movidos:
                            shutil.move(file, ir_para)
                            movidos.append(file)

            except Exception as e:
                print(e)


move_similar('cachorros/')
move_similar('gatos/')
move_similar('casas/')
