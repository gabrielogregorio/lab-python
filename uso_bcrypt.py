# pip install bycrypt
import bcrypt
password = '1234'
password2 = '1236'
senha = str.encode(password)
senha2 = str.encode(password2)
cost = 8
salt_bytes = bcrypt.gensalt(cost)
salt = salt_bytes.decode()
hashed_bytes = bcrypt.hashpw(senha, salt_bytes)
hashed = hashed_bytes.decode()
if (bcrypt.checkpw(senha, hashed_bytes)):
  print("Senha validada")

if (bcrypt.checkpw(senha2, hashed_bytes)):
  pass
else:
  print("Senha Negada corretamente")

print("Salvar no BD")
print('Salt: ', salt)
print("Hash: ", hashed)
print("Pass: ", password)