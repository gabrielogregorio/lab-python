from PIL import Image
import pytesseract
import shutil
import os

# Caminho do Executável
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Move imagens com texto
def move_imagem_com_texto(base):

    # Caminha por todas as imagens
    for file in os.listdir(base):

        # Tenta....
        try:
            # Obter o texto
            juntado = os.path.join(base, file)
            texto =  pytesseract.image_to_string(Image.open(juntado))

            # Se tiver mais de 5 caracteres
            if len(texto) > 5:
                # Move o arquivo com texto para a pasta texto
                shutil.move(juntado, os.path.join(base, 'texto'))
                print(base, texto)

        except Exception as erro:
            print(erro)

move_imagem_com_texto(base = 'baratas/')
move_imagem_com_texto(base = 'ratos/')
