import unittest
import sys
import importlib


if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
filtrar_pares = getattr(modulo, "filtrar_pares")


sys.argv = sys.argv[:1]



class TestFiltrarPares(unittest.TestCase):
    def test_lista_mixta(self):
        """test de lista mixta de pares e impares"""
        self.assertEqual(filtrar_pares([1, 2, 3, 4, 5]), [2, 4])

    def test_solo_impares(self):
        """test de lista de solo impares"""
        self.assertEqual(filtrar_pares([1, 3, 5]), [])

    def test_lista_vacia(self):
        """test de lista vacia"""
        self.assertEqual(filtrar_pares([]), [])

    def test_solo_pares(self):
        """test de lista de solo pares"""
        self.assertEqual(filtrar_pares([2, 4, 6]), [2, 4, 6])



if __name__ == "__main__":
    unittest.main(verbosity=2)