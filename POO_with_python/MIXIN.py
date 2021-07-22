#classe mixin é classe normal em python, mas:

#Quando usar? Quando você quiser reaproveitar código
#Propriedades:
#1) não deve ser extendido
#2) Não deve ser instanciada

# CLASSE MIXIN ELA ESPERA QUE OUTRA CLASSE TENHA OS METODOS E ATRIBUTOS
# E MIXINS NAO TEM INIT

# Guarda conteudo
class Livro(object):
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo


# Não precisa explicitar objeto
# Decora os dados do livro
class LivroHtmlMixin(object):
    def renderizar(self):
        return '<html>{}, {}</html>'.format(self.nome, self.conteudo)


class LivroHtml(Livro, LivroHtmlMixin):
    pass


Livro_html = LivroHtml('Algum Livro', 'texto...')
print(Livro_html.renderizar())
