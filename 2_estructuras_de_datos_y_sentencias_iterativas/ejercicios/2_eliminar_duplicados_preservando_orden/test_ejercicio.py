import unittest
import sys
import importlib


if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
eliminar_duplicados = getattr(modulo, "eliminar_duplicados")


sys.argv = sys.argv[:1]


class TestEliminarDuplicados(unittest.TestCase):
    def test_lista_con_duplicados(self):
        """test de lista con duplicados"""
        self.assertEqual(eliminar_duplicados([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_sin_duplicados(self):
        """test de lista sin duplicados"""
        self.assertEqual(eliminar_duplicados([1, 2, 3]), [1, 2, 3])

    def test_lista_vacia(self):
        """test de lista vacia"""
        self.assertEqual(eliminar_duplicados([]), [])

    def test_duplicados_con_strings(self):
        """test de lista con duplicados de strings"""
        self.assertEqual(eliminar_duplicados(["a", "b", "a", "c"]), ["a", "b", "c"])

    def test_argumento_no_lista(self):
        """test de argumento no lista"""
        with self.assertRaises(TypeError):
            eliminar_duplicados("no es una lista")

        with self.assertRaises(TypeError):
            eliminar_duplicados(123)

        with self.assertRaises(TypeError):
            eliminar_duplicados(None)


if __name__ == "__main__":
    unittest.main(verbosity=2)