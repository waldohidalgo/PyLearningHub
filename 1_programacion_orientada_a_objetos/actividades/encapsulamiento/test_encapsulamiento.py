import unittest
import sys
import importlib

# Obtener nombre del módulo desde argumentos
if len(sys.argv) < 2:
    print("Uso: python test_encapsulamiento.py <nombre_modulo>")
    sys.exit(1)

modulo_nombre = sys.argv[1]
modulo = importlib.import_module(modulo_nombre)
Producto = getattr(modulo, "Producto")

# Eliminar el nombre del módulo de los argumentos de unittest
sys.argv = sys.argv[:1]

class TestProducto(unittest.TestCase):
    def test_precio_valido(self):
        """Test de precio valido"""
        p = Producto()
        p.set_precio(1500)
        self.assertEqual(p.get_precio(), 1500)

    def test_precio_invalido_negativo(self):
        """Test de precio negativo invalido"""
        p = Producto()
        p.set_precio(1000)
        p.set_precio(-200)  
        self.assertEqual(p.get_precio(), 1000)

    def test_precio_invalido_cero(self):
        """Test de precio cero invalido"""
        p = Producto()
        p.set_precio(500)
        p.set_precio(0) 
        self.assertEqual(p.get_precio(), 500)

    def test_precio_invalido_texto(self):
        """Test de precio texto invalido"""
        p = Producto()
        p.set_precio(800)
        p.set_precio("gratis")  
        self.assertEqual(p.get_precio(), 800)

    def test_acceso_directo_precio_privado(self):
        """Test de acceso directo al precio privado"""
        p = Producto()
        with self.assertRaises(AttributeError):
            _ = p.__precio 

if __name__ == '__main__':
    unittest.main(verbosity=2)