import logging

'''
Nível de mensagens
INFO - Nível info
DEBUG - Nivel debug
WARNING - Nível warning, msg importar
ERROR - Mensagem de erros
CRITICAL - Critical => Mensagens criticas, sem espaço em disco, memória cheia...
'''

def execute():
  #Data hora, nome do argumento?, nível
  formatacao = '%(asctime)s - %(name)s %(levelname)s - %(message)s'
  datefmt = '%d/%m/%Y %I:%M:%S %p'
  # Só mostra logs de info
  logging.basicConfig(filename="file.log", level=logging.DEBUG, filemode='w', format=formatacao, datefmt=datefmt)

  # Nome do arquivo com o nome do módulo
  logger = logging.getLogger(__name__)
  # __file__ para o nome do arquivo

  logger.info('Mensagem informativa')
  logger.debug("Mensagem de debug")
  logger.error('Um erro aconteceu')

if __name__ == '__main__':
  execute()