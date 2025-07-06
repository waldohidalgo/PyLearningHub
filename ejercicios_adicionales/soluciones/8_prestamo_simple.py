from typing import List

class Libro:
    def __init__(self, titulo, autor, stock):
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

class LibroNoDisponibleError(Exception):
    pass

class Biblioteca():
    def __init__(self, libros=[]):
        self.libros:List[Libro] = libros

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.stock > 0:
                    libro.stock -= 1
                    return libro
                else:
                    raise LibroNoDisponibleError
                

if __name__ == "__main__":
    biblioteca=Biblioteca([
        Libro("El principito", "Antoine de Saint-Exupery", 5),
        Libro("El Cuerpo", "Franz Kafka", 10),
        Libro("El Quijote", "Miguel de Cervantes",0)
    ])

    print("--Verificación libro sin stock--")
    try:
        libro_prestado=biblioteca.prestar_libro("El Quijote")
        print(libro_prestado)
    except LibroNoDisponibleError:
        print("El libro no esta disponible")

    print("--Verificación prestamo libro con stock--")
    try:
        nombre_libro="El Cuerpo"

        libro_prestado=biblioteca.prestar_libro(nombre_libro)
        print(f"EL libro ha sido prestado. Su stock ahora es: {libro_prestado.stock if libro_prestado else 0}")
    except LibroNoDisponibleError:
        print("El libro no esta disponible")