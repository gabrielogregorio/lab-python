"""
mixin é:
    # Classe comun

Quando ultilizar?
    # Se você desejar reutilizar uma feature
    em um classe diferente

    # Para melhorar a modulaidade

    # Forma mais controlada de adicionar funcionalidades

    # Tem algumas propriedades
        # proprieidades que não devem ser extendidas
        # Não devem ser instanciadas

    # Em Python, o conceito de mixins é implementada
    Usando Herança multipla



"""

# GUARDA ATRIBUTOS
# TEM NOME, CONTEUDO
class Livro(object):
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo

# APLICA COISAS NOS ATRIBUTOS
# NAO APLICA O __INIT__
# NAO DEFINE OS ATRIBUTOS
# ELA ESPERA QUE OS ATRIBUTOS
# TENHAM SIDO DEFINIDOS EM OUTRAS
# CLASSES.
class LivroHtmlMixin(object):
    def renderizar(self):
        return ('<html><head>{}</head><body>{}</body></html>'.format(self.nome, self.conteudo))

# USA HERANCA MULTIPLA PARA COMPOR
# OS ATRIBUTOS DE LIVROS PARA COMPOR
# COM O METODO RENDERIZAR
# CUIDADO COM O AUMENTO DO ACOPLAMENTO
class LivroHtml(Livro, LivroHtmlMixin):
    pass

livro_html = LivroHtml('Perdido em marte', 'texto e.....')
print(livro_html.renderizar())


