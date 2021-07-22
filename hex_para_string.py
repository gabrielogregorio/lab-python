hexCodigo = """7f45 4c46"""

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


