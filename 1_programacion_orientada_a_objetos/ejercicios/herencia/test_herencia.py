import unittest
import sys
import importlib


if len(sys.argv) < 2:
    print("Uso: python test_herencia.py <nombre_modulo_sin_.py>")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)


Figura = getattr(modulo, "Figura")
Rectangulo = getattr(modulo, "Rectangulo")
Circulo = getattr(modulo, "Circulo")

sys.argv = sys.argv[:1] # sin este codigo se genera error

class TestFiguras(unittest.TestCase):
    def test_area_figura_base(self):
        """Prueba que el area de la figura base es 0"""
        f = Figura()
        self.assertEqual(f.area(), 0)

    def test_area_rectangulo(self):
        """Prueba que el area de un rectangulo es 20"""
        r = Rectangulo(4, 5)
        self.assertEqual(r.area(), 20)

    def test_area_circulo(self):
        """Prueba que el area de un circulo es 3.14159"""
        c = Circulo(3)
        import math
        self.assertAlmostEqual(c.area(), math.pi * 9, places=5)

    def test_rectangulo_valores_negativos(self):
        """Prueba que el area de un rectangulo con valores negativos es -10"""
        r = Rectangulo(-2, 5)
        self.assertEqual(r.area(), -10)

if __name__ == "__main__":
    unittest.main(verbosity=2)
