"""
Singleton cria somente um objeto,
mesmo que ele seja instanciado várias vezes

Ele garante a existência de uma unica isntancia da
classe relacionada ao sistema e disponibiliza um
ponto central de acesso global

!!!!!!!!!!!Cuidado com a alteração de variáveis globais!!!!!!!!!!!!!!!
"""

import sqlite3

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, *kwargs)
        return cls._instances[cls]

class DataBase(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('banco.db')

            # Permite navegar e manipular os registros do banco de dados
            self.cursor = self.connection.cursor()

        return self.cursor

db1 = DataBase().connect()
db2 = DataBase().connect()
db3 = DataBase().connect()
print(db1, db2, db3)

"""
<sqlite3.Cursor object at 0x7fce65865ce0>
<sqlite3.Cursor object at 0x7fce65865ce0>
<sqlite3.Cursor object at 0x7fce65865ce0>
"""
