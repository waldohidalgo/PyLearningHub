def es_mayor(edad):
    return edad >= 18

def consulta_edad():
    nombre= input("Ingrese su nombre: ")
   

    while True:
        try:
            edad = int(input("Por favor, introduce tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa. Inténtalo de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número para la edad.")



    if es_mayor(edad):
        print(f"{nombre} es mayor de edad.")
    else:
        print(f"{nombre} es menor de edad.")
    
    
if __name__ == "__main__":
    consulta_edad()
