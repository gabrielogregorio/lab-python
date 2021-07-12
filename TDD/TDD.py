# Faça os testes, depois escreva um código para passar
import unittest
from Calculadora import Calculadora

class TddExemplo(unittest.TestCase):
  def teste_soma(self):
    calc = Calculadora()
    resultado = calc.somar(10, 20)
    self.assertEqual(30, resultado)

  def teste_subtrair(self):
    calc = Calculadora()
    resultado = calc.subtrair(10, 20)
    self.assertEqual(-10, resultado)


if __name__ == '__main__':
  unittest.main()