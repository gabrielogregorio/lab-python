hexCodigo = """7f45 4c46 0201 0100 0000 0000 0000 0000
0200 3e00 0100 0000 1008 4000 0000 0000
4000 0000 0000 0000 b01c 0000 0000 0000
0000 0000 4000 3800 0900 4000 1f00 1c00
0600 0000 0500 0000 4000 0000 0000 0000
"""

hexCodigo = str(hexCodigo)

hexCodigo = hexCodigo.replace(' ','')  # remove espaços
hexCodigo = hexCodigo.replace('\n','') # remove linhas

string = ''
i = 0
while i < len(hexCodigo):
    try:
        string += bytes.fromhex( hexCodigo[i:i+4]).decode('utf8')
    except Exception as erro:
        print(erro)
    i += 6

print(string)


