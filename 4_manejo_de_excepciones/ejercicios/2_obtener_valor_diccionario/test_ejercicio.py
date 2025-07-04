import unittest
import sys
import importlib

if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
obtener_valor = getattr(modulo, "obtener_valor")


sys.argv = sys.argv[:1]

class TestDiccionarios(unittest.TestCase):
    def setUp(self):
        self.datos = {"nombre": "Waldo", "edad": 30}


    def test_argumento_no_diccionario(self):
        """Prueba que se lance una excepción si el argumento no es un diccionario."""
        with self.assertRaises(TypeError):
            obtener_valor("no es un diccionario", "clave")

    def test_clave_existente(self):
        """Prueba que la clave "nombre" exista en el diccionario."""
        self.assertEqual(obtener_valor(self.datos, "nombre"), "Waldo")

    def test_clave_inexistente(self):
        """Prueba que la clave "correo" no exista en el diccionario."""
        with self.assertRaises(KeyError):
            obtener_valor(self.datos, "correo")

if __name__ == "__main__":
    unittest.main(verbosity=2)
