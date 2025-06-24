import unittest
import sys
import importlib


if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
mostrar_datos = getattr(modulo, "mostrar_datos")
cliente=getattr(modulo, "cliente")

sys.argv = sys.argv[:1]



class TestMostrarDatos(unittest.TestCase):
    def test_mostrar_datos_argumento_invalido(self):
        """ Comprueba que el argumento sea un diccionario """
        with self.assertRaises(TypeError):
            mostrar_datos("no es un diccionario")

        with self.assertRaises(TypeError):
            mostrar_datos(123)

        with self.assertRaises(TypeError):
            mostrar_datos(["Luis", 25, "Santiago"])

        with self.assertRaises(TypeError):
            mostrar_datos(None)
    def test_diccionario_estructura_y_valores(self):
        """ Comprueba que el diccionario tenga las keys correctas y los valores correctos """
        self.assertIn("edad", cliente)
        self.assertIn("nombre", cliente)
        self.assertIn("ciudad", cliente)

        
        self.assertEqual(cliente["edad"], 25)
        self.assertEqual(cliente["nombre"], "Luis")
        self.assertEqual(cliente["ciudad"], "Santiago")

    def test_mostrar_datos_salida(self):
        """ Comprueba que la salida sea la correcta """
        resultado = mostrar_datos(cliente)
        esperado = "Cliente Luis, 25 años, de Santiago"
        self.assertEqual(resultado, esperado)    





if __name__ == "__main__":
    unittest.main(verbosity=2)