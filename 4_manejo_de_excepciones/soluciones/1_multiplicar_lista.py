def multiplicar_lista(lista, factor):
    if not isinstance(lista, list):
        raise TypeError("El primero parámetro debe ser una lista.")
    
    if not isinstance(factor, (int, float)):
        raise TypeError("El segundo parámetro debe ser un número.")
    
    resultado = []
    for item in lista:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Elemento inválido: {item} no es un número.")
        resultado.append(item * factor)
    return resultado