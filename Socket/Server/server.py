import socket

# IPV4, TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[<>] Servidor aguardando cliente")
server.bind(('localhost', 7777))
server.listen(1) # Ouvir uma conexão

connection, address = server.accept() # Aceitar conexão
print("[OK] Cliente conectado")
namefile = connection.recv(1024).decode()

with open(namefile, 'rb') as file:
  for data in file.readlines():
    connection.send(data)
    print('[=>] Enviando arquivo')

  print("[OK] Arquivo Enviado")

