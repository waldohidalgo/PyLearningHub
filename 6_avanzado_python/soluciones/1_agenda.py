class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        if not nombre or not telefono:
            raise ValueError("Nombre y teléfono no pueden estar vacíos.")
        self.contactos[nombre.lower()] = telefono

    def obtener_telefono(self, nombre):
        try:
            return self.contactos[nombre.lower()]
        except KeyError:
            raise KeyError(f"El contacto '{nombre}' no existe.")

    def eliminar_contacto(self, nombre):
        if nombre.lower() in self.contactos:
            del self.contactos[nombre.lower()]
        else:
            raise KeyError(f"El contacto '{nombre}' no se puede eliminar porque no existe.")

    def listar_contactos(self):
        return dict(sorted(self.contactos.items()))
