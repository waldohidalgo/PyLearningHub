from operaciones import sumar, restar, multiplicar, dividir

def ejecutar_calculadora():
    print("Operaciones disponibles: sumar, restar, multiplicar, dividir")
    operacion = input("¿Qué operación deseas realizar?: ").strip().lower()

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if operacion == "sumar":
        print("Resultado:", sumar(a, b))
    elif operacion == "restar":
        print("Resultado:", restar(a, b))
    elif operacion == "multiplicar":
        print("Resultado:", multiplicar(a, b))
    elif operacion == "dividir":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida.")


if __name__ == "__main__":
    ejecutar_calculadora()