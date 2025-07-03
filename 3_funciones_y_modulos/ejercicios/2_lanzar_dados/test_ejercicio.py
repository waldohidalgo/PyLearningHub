import unittest
import sys
import importlib

if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
lanzar_dados = getattr(modulo, "lanzar_dados")


sys.argv = sys.argv[:1]

class TestJuegos(unittest.TestCase):
    def test_un_dado(self):
        """Lanza un dado con valor aleatorio entre 1 y 6"""
        resultado = lanzar_dados(1)
        self.assertEqual(len(resultado), 1)
        self.assertTrue(1 <= resultado[0] <= 6)

    def test_varios_dados(self):
        """Lanza varios dados con valores aleatorios entre 1 y 6"""
        resultado = lanzar_dados(5)
        self.assertEqual(len(resultado), 5)
        for valor in resultado:
            self.assertTrue(1 <= valor <= 6)

    def test_error_dado_invalido(self):
        """Comprueba que se lanza un error si se pasa un número de dados inválido"""
        with self.assertRaises(ValueError):
            lanzar_dados(0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
