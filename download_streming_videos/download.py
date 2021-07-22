import os
import time
import pyautogui
import requests
import shutil
import re

class BaixarVideos():
    """ Serve para baixar vídeos em streaming, como de plataformas de cursos. Dependendo da plataforma podem haver termos contra isso, portanto, não use esse programa para baixar vídeos de plataformas que não permite """
    def __init__(self, cdn:str, i:int=1, f:int=999):
        self.cdn = cdn
        self.i = i
        self.f = f

    def baixar(self):
        for x in range(self.i, self.f):
            base = self.cdn.format(x)

            os.system('chrome.exe  "{}"'.format(base))
            time.sleep(0.1)

            while True:
                try:
                    pos = pyautogui.locateOnScreen('save.png', grayscale=True, confidence=0.98)
                    pyautogui.click(pos.left+10, pos.top+4)
                    pyautogui.moveTo(x=275, y=80)
                    break

                except Exception as e:
                    print('ops', e)

        return True


class UnirVideos():
    def __init__(self, dir_files, name_merged):
        self.cwd = os.getcwd()
        self.dir_files = dir_files
        self.name_merged = name_merged

    def unir(self):
        # Obter lista de arquivos ts
        lista = []
        for ts_file in os.listdir('{}/{}'.format(self.cwd, self.dir_files)):
            lista.append(ts_file)

        # Ordenar os vídeos
        lista = sorted(lista, key=self.keyFunc)

        # Unir os vídeos
        with open(self.name_merged, 'wb') as merged:
            for ts_file in lista:
                with open(f'{self.cwd}/{self.dir_files}/{ts_file}', 'rb') as mergefile:
                    shutil.copyfileobj(mergefile, merged)

    def keyFunc(self, afilename):
        nondigits = re.compile("\\D")
        return int(nondigits.sub("", afilename))



#b = BaixarVideos('', 1, 999)
#b.baixar()

#m = UnirVideos('files', 'merged.ts')
#m.unir()
