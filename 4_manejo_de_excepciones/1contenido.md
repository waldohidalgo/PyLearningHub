# Manejo de Excepciones

## Tabla de Contenidos

- [Manejo de Excepciones](#manejo-de-excepciones)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Sintaxis](#sintaxis)
  - [Manejo de cualquier tipo de excepción](#manejo-de-cualquier-tipo-de-excepción)
  - [Manejo de excepciones particulares](#manejo-de-excepciones-particulares)
  - [Lanzamiento de Excepciones](#lanzamiento-de-excepciones)

## Sintaxis

Una excepción es un error que ocurre durante la ejecución de un programa. Cuando se produce una excepción, se interrumpe el flujo normal del programa, impidiendo su uso y Python lanza un mensaje de error (Traceback), a menos que el error sea manejado adecuadamente. A continuación se muestra un código de ejemplo que arroja error:

```py
int('ds')
```

El error que se muestra es del tipo: `ValueError: invalid literal for int() with base 10: 'ds'`

Para evitar que se interrumpa el flujo normal del programa, es posible manejar las excepciones con bloques `try` y `except`. La sintaxis básica es la siguiente:

```py
try:
    # código que puede lanzar una excepción
except TipoDeExcepcion:
    # código que se ejecuta si ocurre la excepción
```

Cuando en el bloque `try` no ocurre ninguna excepción, es posible utilizar un bloque `else`:

```py
try:
    # código que puede lanzar una excepción
except TipoDeExcepcion:
    # código que se ejecuta si ocurre la excepción
else:
    # código que se ejecuta si el try no arroja alguna excepción
```

También existe un bloque `finally` que se ejecuta siempre ya sea ocurra o no ocurra una excepción:

```py
try:
    # código que puede lanzar una excepción
except TipoDeExcepcion:
    # código que se ejecuta si ocurre la excepción
else:
    # código que se ejecuta si el try no arroja alguna excepción
finally:
    # código que se ejecuta siempre ya sea si se gatilla o no una excepción
```

A continuación, se muestra un ejemplo aplicando la sintaxis anterior:

```py
try:
    numero = int(input("Ingresa un número"))
    print(f"El Doble es: {numero * 2}")
except ValueError:
    print("El número ingresado no es válido")
```

## Manejo de cualquier tipo de excepción

Para manejar cualquier tipo de excepción es posible utilizar la clase `Exception`:

```py
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Ocurrió un error: {e}")
```

## Manejo de excepciones particulares

Es posible manejar cada tipo de excepción de manera aislada creando un bloque except para cada tipo. La sintaxis es la siguiente:

```py
try:
    # código que puede lanzar una excepción
except TipoDeExcepcion1:
    # código que se ejecuta si ocurre la excepción de tipo 1
except TipoDeExcepcion2:
    # código que se ejecuta si ocurre la excepción de tipo 2
except TipoDeExcepcion3:
    # código que se ejecuta si ocurre la excepción de tipo 3
```

## Lanzamiento de Excepciones

Es posible utilizar la palabra reservada `raise` para lanzar excepciones cuando se desee. El siguiente código muestra un ejemplo:

```py
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b
```
