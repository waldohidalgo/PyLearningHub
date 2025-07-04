import unittest
import sys
import importlib

if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
multiplicar_lista = getattr(modulo, "multiplicar_lista")


sys.argv = sys.argv[:1]

class TestListas(unittest.TestCase):
    def test_lista_valida(self):
        """Multiplica lista compuesta por valores enteros"""
        self.assertEqual(multiplicar_lista([1, 2, 3], 2), [2, 4, 6])

    def test_lista_con_float(self):
        """Multiplica lista compuesta por valores enteros y decimales"""
        self.assertEqual(multiplicar_lista([1.5, 2.0], 2), [3.0, 4.0])

    def test_lista_con_str(self):
        """Multiplica lista compuesta por valores no numéricos"""
        with self.assertRaises(TypeError):
            multiplicar_lista([1, "dos", 3], 2)

    def test_entrada_no_lista(self):
        """Test de entrada para ingreso de objeto que no es lista"""
        with self.assertRaises(TypeError):
            multiplicar_lista("123", 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
