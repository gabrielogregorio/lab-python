from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):
	@abstractmethod
	def descricao(self):
		pass


class SecaoPessoal(Secao):
	def descricao(self):
		print('Seção Pessoal')

class SecaoAlbum(Secao):
	def descricao(self):
		print('Seção Album')

class SecaoPatente(Secao):
	def descricao(self):
		print('Seção Patente')

class SecaoPublicar(Secao):
	def descricao(self):
		print('Seção Publicar')

class Perfil(metaclass=ABCMeta):
	def __init__(self):
		self.secoes = []
		self.criar_perfil()

	@abstractmethod
	def criar_perfil(self):
		pass

	def obter_secoes(self):
		return self.secoes

	def add_secoes(self, secao):
		self.secoes.append(secao)

class Facebook(Perfil):
	def criar_perfil(self):
		self.add_secoes(SecaoPessoal())
		self.add_secoes(SecaoPatente())
		self.add_secoes(SecaoPublicar())

class Twiter(Perfil):
	def criar_perfil(self):
		self.add_secoes(SecaoAlbum())
		self.add_secoes(SecaoPessoal())

if __name__ == '__main__':
	tipo_perfil = 'Facebook'
	perfil = eval(tipo_perfil)()
	print(perfil.obter_secoes())

	tipo_perfil = 'Twiter'
	perfil = eval(tipo_perfil)()
	print(perfil.obter_secoes())













