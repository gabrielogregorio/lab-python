from PIL import Image
import pytesseract
import shutil
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def move_imagem_com_texto(base):
    for file in os.listdir(base):
        try:
            juntado = os.path.join(base, file)
            texto =  pytesseract.image_to_string(Image.open(juntado))

            if len(texto) > 5:
                shutil.move(juntado, os.path.join(base, 'texto\\'))
                print(base, texto)

        except Exception as erro:
            print(erro)

move_imagem_com_texto(base = 'avioes\\')