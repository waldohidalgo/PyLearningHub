def obtener_valor(diccionario, clave):
    if not isinstance(diccionario, dict):
        raise TypeError("El argumento 'diccionario' debe ser un diccionario.")
    if clave not in diccionario:
        raise KeyError(f"La clave '{clave}' no existe en el diccionario.")
    return diccionario[clave]

