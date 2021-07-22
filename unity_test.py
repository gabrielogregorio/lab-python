import unittest
import sys

class ConverteNumeroRomano:
    def __init__(self):
        self.digito_map = {"M": 1000, "D":500, "C": 100, "L": 50, "X": 10, "V":5, "I": 1}

    
    def converter_para_decimal(self, numero_romano):
        val = 0

        for char in numero_romano:
            val += self.digito_map[char]
        
        return val
    

class TestConverteNumeroRomano(unittest.TestCase):

    # Antes de cada teste
    def setUp(self):
        #print('Contruir o objeto da classe')
        self.cnr = ConverteNumeroRomano()
    
    # Depois de cada teste
    def tearDown(self):
        #print('Destruiu o objeto da classe')
        self.cnr = None

    # Pula um teste
    @unittest.skip('Testando Skip')
    def test_mil(self):
        print('teste mil')
        self.assertEqual(1000, self.cnr.converter_para_decimal('M'))

    @unittest.skipIf(sys.version_info > (2,7), "Não suporta versões superiores a 2.7")
    def test_cem(self):
        print('teste cem')
        self.assertEqual(100, self.cnr.converter_para_decimal('C'))

    def test_cinquenta(self):
        print('teste cinquenta')
        self.assertEqual(50, self.cnr.converter_para_decimal('L'))
    
    def test_vazio(self):
        print('teste vazio')
        self.assertTrue(self.cnr.converter_para_decimal('') == 0)
        self.assertFalse(self.cnr.converter_para_decimal('') > 0)

    
if __name__ == '__main__':
    unittest.main()


#  python .\unity_test.py -v
# v para er em detalhes