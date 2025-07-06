import unittest
import sys
import importlib
from unittest.mock import patch


if len(sys.argv) < 2:
    print("Uso: python test_ejercicio.py ejercicio")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
Agenda = getattr(modulo, "Agenda")


sys.argv = sys.argv[:1]

class TestAgenda(unittest.TestCase):

    def setUp(self):
        self.agenda = Agenda()
        self.agenda.agregar_contacto("Ana", "12345")
        self.agenda.agregar_contacto("Luis", "67890")

    def test_agregar_contacto(self):
        """
        Verificar que se puede agregar un contacto a la agenda."""
        self.agenda.agregar_contacto("Pedro", "11111")
        self.assertEqual(self.agenda.obtener_telefono("Pedro"), "11111")

    def test_agregar_contacto_vacio(self):
        """
        Verificar que no se puede agregar un contacto con nombre vacio."""
        with self.assertRaises(ValueError):
            self.agenda.agregar_contacto("", "123")

    def test_obtener_telefono_existente(self):
        """
        Verificar que se puede obtener el telefono de un contacto existente."""
        self.assertEqual(self.agenda.obtener_telefono("Ana"), "12345")

    def test_obtener_telefono_inexistente(self):
        """
        Verificar que se lanza una excepcion del tipo KeyError si se intenta obtener el telefono de un contacto inexistente."""
        with self.assertRaises(KeyError):
            self.agenda.obtener_telefono("Maria")

    def test_eliminar_contacto(self):
        """
        Verificar que se puede eliminar un contacto de la agenda."""
        self.agenda.eliminar_contacto("Luis")
        with self.assertRaises(KeyError):
            self.agenda.obtener_telefono("Luis")

    def test_eliminar_inexistente(self):
        """
        Verificar que se lanza una excepcion del tipo KeyError si se intenta eliminar un contacto inexistente."""
        with self.assertRaises(KeyError):
            self.agenda.eliminar_contacto("NoExiste")

    def test_listar_contactos(self):
        """
        Verificar que se puede listar los contactos de la agenda."""
        contactos = self.agenda.listar_contactos()
        self.assertEqual(list(contactos.keys()), ["ana", "luis"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
