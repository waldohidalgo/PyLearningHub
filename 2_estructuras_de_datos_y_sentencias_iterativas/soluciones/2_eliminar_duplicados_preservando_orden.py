def eliminar_duplicados(lista):
    if type(lista) != list:
        raise TypeError("El argumento debe ser una lista")
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)
    return resultado