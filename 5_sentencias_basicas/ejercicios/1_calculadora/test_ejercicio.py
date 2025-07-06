import unittest
import sys
import importlib
from unittest.mock import patch


if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
sumar = getattr(modulo, "sumar")
restar= getattr(modulo, "restar")
multiplicar= getattr(modulo, "multiplicar")
dividir= getattr(modulo, "dividir")
ejecutar_calculadora = getattr(modulo, "ejecutar_calculadora")

sys.argv = sys.argv[:1]


class TestCalculadoraOperaciones(unittest.TestCase):

    def test_sumar(self):
        """Prueba la operación de suma."""
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        """Prueba la operación de resta."""
        self.assertEqual(restar(5, 2), 3)

    def test_multiplicar(self):
        """Prueba la operación de multiplicación."""
        self.assertEqual(multiplicar(4, 3), 12)

    def test_dividir(self):
        """Prueba la operación de división."""
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        """Verifica que se lanza una excepción al intentar dividir por cero."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

class TestCalculadoraInteraccion(unittest.TestCase):

    @patch('builtins.input', side_effect=['sumar', '4', '5'])
    @patch('builtins.print')
    def test_ejecutar_suma(self, mock_print, mock_input):
        """Prueba la ejecución de la operación de suma."""
        ejecutar_calculadora()
        mock_print.assert_any_call("Resultado:", 9.0)

    @patch('builtins.input', side_effect=['dividir', '10', '0'])
    @patch('builtins.print')
    def test_ejecutar_division_por_cero(self, mock_print, mock_input):
        """Verifica que se lanza una excepción al intentar dividir por cero."""
        with self.assertRaises(ZeroDivisionError):
            ejecutar_calculadora()

    @patch('builtins.input', side_effect=['potenciar', '2', '3'])
    @patch('builtins.print')
    def test_operacion_invalida(self, mock_print, mock_input):
        """Verifica que se muestra un mensaje de operación no válida."""
        ejecutar_calculadora()
        mock_print.assert_any_call("Operación no válida.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
