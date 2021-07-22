import sqlite3

class BancoDeDados:
    """ Classe que representa o banco de dados """
    def __init__(self, nome="banco_aula1.db"):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """ Conecta ao banco de dados"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """ Desconecta do banco de dados"""
        try:
            self.conexao.close()
        except AttributeError:
            pass
