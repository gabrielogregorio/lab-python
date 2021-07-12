import unittest
#  pip install nose --user
# nosetests .\modulo_noise\ -v
# Realiza um teste geral

from classe import Retornar

class TestadorClasse(unittest.TestCase):
  def test_false(self):
    value = Retornar().retornar()
    self.assertEquals(True, value)