# sudo pip3 install pyqrcode

import pyqrcode

q = pyqrcode.create('Isso é um QR CODE')
q.svg('img.svg', scale=4)
q.png('img.png',scale=10)


