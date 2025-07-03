# Funciones y Módulos

## Tabla de Contenidos

- [Funciones y Módulos](#funciones-y-módulos)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [1.Funciones](#1funciones)
    - [1.1.Parámetros y argumentos](#11parámetros-y-argumentos)
    - [1.2.Valores por defecto](#12valores-por-defecto)
    - [1.3.Funciones con número variable de argumentos](#13funciones-con-número-variable-de-argumentos)
    - [1.4.Funciones anónimas (lambda)](#14funciones-anónimas-lambda)
  - [2.Módulos](#2módulos)

## 1.Funciones

Una función es un bloque reutilizable de código que realiza una tarea específica. Ayuda a dividir un programa en partes más pequeñas, más legibles y más fáciles de mantener. La sintaxis básica para crear funciones es la siguiente donde es posible retornar algo o nada, en tal caso, el retorno queda implicito como `None`:

```py
def nombre_de_funcion(parámetros):
    # bloque de código
    return resultado
```

A continuación, se muestra un ejemplo creando la función `saludar` la cual retorna una cadena.

```py
def saludar(nombre):
    return f"Hola, {nombre}!"
```

### 1.1.Parámetros y argumentos

- Parámetros: son variables definidas en la declaración de la función.

- Argumentos: son los valores reales pasados a la función al momento de llamarla.

A continuación, se muestra un ejemplo en el cual se crea la función `sumar` con los parámetros `a` y `b`, luego la función es llamada utilizando los argumentos 3 y 5, respectivamente.

```py
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)
```

Al momento de invocar la función es posible utilizar nombres para asignar cada argumento a cada parámetro. Por ejemplo:

```py
def sumar(a, b):
    return a + b

resultado = sumar(b=3, a=5)
print(resultado)
```

### 1.2.Valores por defecto

Es posible asignar valores por defecto a los parámetros al momento de definir la función. Por ejemplo, a continuación se crea la función `saludar` con el parámetro nombre con el valor por defecto igual a `invitado`.

```py
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()           # Hola, invitado
saludar("María")    # Hola, María
```

Es posible combinar parámetros sin y con valores por defecto. En tal caso, los parámetros con valores por defecto deben ir a continuación de los parámetros sin valores por defecto. En caso contrario se genera un `SyntaxError`.

### 1.3.Funciones con número variable de argumentos

Es posible utilizar un número variable de argumentos los cuales son pasados como tupla a la función al momento de su invocación. En tal caso, al momento de la definición de la función se debe utilizar la siguiente sintaxis:

```py
def nombre_funcion(*args):
    #contenido
    pass
```

La palabra args es una convención que representa a la tupla de elementos utilizados al invocar la función.

A continuación, se muestra un ejemplo de aplicación de lo anterior:

```py
def mostrar_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

mostrar_nombres("Ana", "Luis", "Carlos")
```

También es posible utilizar un número variable de argumentos nombrados para lo cual se utilizará la siguiente sintaxis:

```py
def nombre_funcion(**kwargs):
    #contenido
    pass
```

La palabra kwargs es una convención que representa al diccionario de elementos utilizados al invocar la función. Por ejemplo:

```py
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Lucía", edad=25)
```

Es posible combinar un número variable de argumentos sin y con nombre para lo cual se utiliza la siguiente notación:

```py
def nombre_funcion(*args,**kwargs):
    #contenido
    pass
```

### 1.4.Funciones anónimas (lambda)

Se denomina funciones anónimas a aquellas que son creadas en una sola línea utilizando la siguiente sintaxis:

```py
lambda parámetros: expresión
```

Por ejemplo:

```py
suma = lambda a, b: a + b
print(suma(3, 4))
```

## 2.Módulos

Un módulo es un archivo .py que contiene definiciones de diversos objetos como funciones, clases, constantes y variables que se pueden importar y reutilizar en otros scripts. A continuación, se muestra un ejemplo creando el archivo `mimodulo.py` que contiene dos funciones:

```py
def saludar(nombre):
    return f"Hola, {nombre}"

def despedir(nombre):
    return f"Adiós, {nombre}"
```

Para utilizar el módulo es necesario importarlo desde otro archivo:

```py
import mimodulo

print(mimodulo.saludar("Luis"))
```

Python incluye una gran colección de módulos estándar o built-in (como math, datetime, random, etc.). Es posible utilizar la palabra clave `from` para importar objetos específicos del módulo y renombrar el objeto utilizando la palabra clave `as`.

Cuando existe código que se ejecuta en el mismo módulo y que no se desea ejecutar al importarlo es posible utilizar la siguiente expresión para envolver el código que se ejecuta en el mismo módulo:

```py
if __name__ == "__main__":
    # codigo que se ejecuta en el mismo módulo
```
