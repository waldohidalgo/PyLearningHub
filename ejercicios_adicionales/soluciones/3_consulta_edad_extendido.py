def verificar_beneficio(edad, pais):
    paises_elegibles = ["argentina", "chile", "colombia"]
    return edad >= 18 and pais.lower() in paises_elegibles

def main():
    nombre = input("Por favor, introduce tu nombre: ")
    while True:
        try:
            edad = int(input("Por favor, introduce tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Valor ingresado inválido. Por favor, introduce un número para la edad.")
    pais = input("Por favor, introduce tu país de residencia: ")

    mensaje = f"Hola {nombre}. Tienes {edad} años y vives en {pais}."
    print(mensaje)

    
    if verificar_beneficio(edad, pais):
        print("¡Felicidades! Eres elegible para acceder al beneficio especial.")
    else:
        print("Lo sentimos, no cumples los requisitos para el beneficio especial en este momento.")

if __name__ == "__main__":
    main()