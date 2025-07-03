import unittest
import sys
import importlib

if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
celsius_a_fahrenheit = getattr(modulo, "celsius_a_fahrenheit")


sys.argv = sys.argv[:1]



class TestConversion(unittest.TestCase):
    def test_cero_celsius(self):
        """Cero grados celsius son 32 grados fahrenheit"""
        self.assertEqual(celsius_a_fahrenheit(0), 32)

    def test_negativo(self):
        """-40 grados celsius son -40 grados fahrenheit"""
        self.assertEqual(celsius_a_fahrenheit(-40), -40)

    def test_valor_decimal(self):
        """36.6 grados celsius son 97.88 grados fahrenheit"""
        self.assertAlmostEqual(celsius_a_fahrenheit(36.6), 97.88, places=2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
