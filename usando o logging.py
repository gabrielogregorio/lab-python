import debug_loggin
import logging

class Usuario:
    def __init__(self, usuario, senha):
        self.senha = senha
        self.usuario = usuario
        self.dict_user = {1: 'user1', 2:'user2'}
        formatacao = '%(asctime)s - %(name)s %(levelname)s - %(message)s'
        datefmt = '%d/%m/%Y %I:%M:%S %p'
        logging.basicConfig(
            #filename="file.log",
            level=logging.INFO,
            filemode='w',
            format=formatacao,
            datefmt=datefmt)
        self.logger = logging.getLogger(__name__)


    def alterar_senha(self, senha_nova):
        self.senha = senha_nova
        self.logger.info('Senha Alterada!')

    def autentica(self, usuario, senha):
        if self.usuario != usuario or self.senha != senha:
            self.logger.warning("Tentativa de acesso invalidada")
            return False
        return True

    def get_usuario_by_id(self, usuario_id):
        user = self.dict_user.get(usuario_id)
        if user is None:
            self.logger.error("Usuário id não existe {}".format(usuario_id))
            return False
        return user


    def abrir_arquivo(self, link):
        try:
            with open('Olá mundo.txt', 'r') as f:
                f.read()
        except Exception as error:
            self.logger.exception("Error")

    def algoritimo(self):
        self.logger.debug('Dados do algoritimo')
    
  
if __name__ == '__main__':
    user = Usuario("ademir", 'ademin')
    user.alterar_senha('admin')
    user.autentica('ademir', 'admin1')
    user.get_usuario_by_id('0')
    user.abrir_arquivo('olá.txt')
    user.algoritimo()
    debug_loggin.execute()