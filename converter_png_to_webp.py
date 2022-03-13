from PIL import Image
import os

try:
   os.mkdir('./webp')
except:
   pass


def convertToWebp(file, quality=70):
  img = Image.open(file).convert('RGB')
  img.save('webp/{}.webp'.format(file), format = "webP",  quality=quality)

listOfImages = os.listdir('./')

for file in listOfImages:
    if file.endswith('.png'):
        convertToWebp(file)
