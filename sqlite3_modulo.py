import sqlite3
import os
os.remove('database.db')

db = sqlite3.connect('database.db')

c = db.cursor()
sql = """

create table alunos
(
    id integer,
    nome text,
    price real
)

"""
c.execute(sql)
db.commit()


estoque = [
	(1, 'notebook', 2451.32),
	(2, 'whois', 3000.00),
	(3, 'macbook', 10900.99),
	(4, 'laptop', 700.00)
	]

c.executemany('insert into alunos values (?, ?, ?)', estoque)

for row in db.execute('select * from alunos'):
	print(row)
