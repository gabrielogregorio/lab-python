import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7777))
print("[OK] Conectado ao servidor")

namefile = str(input('Arquivo>'))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
  while 1:
    data = client.recv(100000000)
    print("[=>] Recebendo Arquivo")
    if not data:
      break
    file.write(data)

print("[OK] Arquivo recebido")
