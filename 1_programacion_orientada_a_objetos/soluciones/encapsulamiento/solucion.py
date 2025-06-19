
class Producto:
    def __init__(self):
        self.__precio = 0

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido.")

    def get_precio(self):
        return self.__precio
    

