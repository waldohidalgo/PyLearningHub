cliente={"edad": 25, "nombre": "Luis", "ciudad": "Santiago"}

def mostrar_datos(cliente):
    if not isinstance(cliente, dict):
        raise TypeError("El argumento debe ser un diccionario")

    datos = {}
    for clave in ['nombre', 'edad', 'ciudad']:
        if clave not in cliente:
            raise KeyError(f"Falta la clave '{clave}'")
        datos[clave] = cliente[clave]

    return f"Cliente {datos['nombre']}, {datos['edad']} años, de {datos['ciudad']}"