import unittest
import sys
import importlib


if len(sys.argv) < 2:
    print("Uso: python test_polimorfismo.py <nombre_modulo>")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)

Empleado = getattr(modulo, "Empleado")
Desarrollador = getattr(modulo, "Desarrollador")
Gerente = getattr(modulo, "Gerente")
calcular_total_bonos = getattr(modulo, "calcular_total_bonos")


sys.argv = sys.argv[:1] # sin este codigo se genera error

class TestPolimorfismo(unittest.TestCase):
    def test_bonus_empleado_base(self):
        """
        El empleado base no tiene bono"""
        e = Empleado("Luis", 1000)
        self.assertEqual(e.calcular_bonus(), 0)

    def test_bonus_desarrollador(self):
        """
        El desarrollador tiene un bono del 20%"""
        d = Desarrollador("Ana", 2000)
        self.assertEqual(d.calcular_bonus(), 400)

    def test_bonus_gerente(self):
        """
        El gerente tiene un bono del 40%"""
        g = Gerente("Waldo", 3000)
        self.assertEqual(g.calcular_bonus(), 1200)

    def test_total_bonos(self):
        empleados = [
            Desarrollador("Ana", 2000),   # 400
            Gerente("Carlos", 3000),      # 1200
            Empleado("Luis", 1000),       # 0
        ]
        total = calcular_total_bonos(empleados)
        self.assertEqual(total, 1600)

if __name__ == "__main__":
    unittest.main(verbosity=2)
