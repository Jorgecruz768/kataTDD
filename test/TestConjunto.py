import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_promedio_un_elemento(self):
        conjunto = Conjunto([10])
        self.assertEqual(conjunto.promedio(), 10)

    def test_promedio_dos_elementos(self):
        conjunto = Conjunto([10, 20])
        self.assertEqual(conjunto.promedio(), 15)

    def test_promedio_varios_elementos(self):
        conjunto = Conjunto([10, 20, 30, 40])
        self.assertEqual(conjunto.promedio(), 25)

if __name__ == '__main__':
    unittest.main()
