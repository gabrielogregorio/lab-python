b64 = b''

import base64

with open("nat.png", "wb") as file:
    file.write(base64.decodebytes(b64))
