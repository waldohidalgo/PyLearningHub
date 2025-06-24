# Estructuras de Datos y Sentencias Iterativas

## Tabla de Contenidos

- [Estructuras de Datos y Sentencias Iterativas](#estructuras-de-datos-y-sentencias-iterativas)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Estructuras de Datos](#estructuras-de-datos)
    - [1. Listas](#1-listas)
      - [1.1 Operaciones más comunes](#11-operaciones-más-comunes)
    - [2.Diccionarios](#2diccionarios)
      - [2.1 Operaciones más comunes](#21-operaciones-más-comunes)
    - [3.Conjuntos](#3conjuntos)
      - [3.1 Operaciones más comunes](#31-operaciones-más-comunes)
    - [4. Tuplas](#4-tuplas)
      - [4.1 Operaciones más comunes](#41-operaciones-más-comunes)
  - [Sentencias Iterativas](#sentencias-iterativas)
    - [1.Ciclo For](#1ciclo-for)
      - [Ejemplos](#ejemplos)
    - [2.Ciclo While](#2ciclo-while)
      - [Ejemplos](#ejemplos-1)
  - [Sentencias Condicionales](#sentencias-condicionales)
    - [Operadores de comparación](#operadores-de-comparación)
    - [Operadores lógicos](#operadores-lógicos)
    - [Ejemplos](#ejemplos-2)
  - [Comprehensions](#comprehensions)
    - [Comprehension de Listas](#comprehension-de-listas)
      - [Ejemplo](#ejemplo)
    - [Comprehension de Conjuntos](#comprehension-de-conjuntos)
      - [Ejemplo](#ejemplo-1)
    - [Comprehension de Diccionarios](#comprehension-de-diccionarios)
      - [Ejemplo](#ejemplo-2)

Se cubrirán los fundamentos de estructuras de datos en Python —listas, diccionarios, conjuntos— y cómo utilizarlas con **sentencias iterativas** como `for` y `while` y **sentencias condicionales** como `if`, `else` y `elif`

## Estructuras de Datos

### 1. Listas

Una **lista** es una colección ordenada y modificable de elementos. Se dice que una lista es **mutable** debido a que sus elementos pueden ser alterados después de su creación. Para crear una lista se utiliza la notación `[]` donde cada elemento que pertenece a la lista se muestra dentro de los corchetes, también se utiliza la función `list` que permite convertir iterables a listas. Para acceder a cada elemento de la lista se utiliza un índice númerico.

A continuación, se muestran ejemplos de creación de listas:

```python
lista_desde_corchetes = [1, 2, 3, "a", True]
lista_desde_cadena=list("Python")
```

#### 1.1 Operaciones más comunes

Las operaciones más comunes en listas son las siguientes:

```python
lista=[1,2,3,4]

lista[1] # acceso a elementos de la lista
lista[2]=45 # modificación de valores de la lista
lista.append(5) # inserción de elemento al final de la lista
del lista[0] # eliminación de elemento en la lista
len(lista) # obtiene el largo de la lista
```

### 2.Diccionarios

Un **diccionario** es una estructura de datos que permite almacenar información **en pares clave-valor**. Es muy útil cuando se necesita acceder a los datos por un identificador único en lugar de un índice numérico como en las listas.

Cada elemento del diccionario tiene:

- Una **clave** (key): puede ser `str`, `int`, `bool`, etc. Debe ser de tipo inmutable.
- Un **valor** (value): puede ser cualquier tipo de dato.

La clave debe ser única. Si se repite una clave, se sobrescribe el valor anterior. Los diccionarios pueden ser creados utilizando paréntesis del tipo `{}` o la función `dict`.

#### 2.1 Operaciones más comunes

Un ejemplo de creación de diccionario es el siguiente:

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Santiago"
}
```

Un listado de las operaciones más comunes se muestra a continuación:

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Santiago",
    78:51,
}  # creación de diccionario


persona[78] # acceso no seguro a valores del diccionario
persona.get(78,"no existe la key") # acceso seguro a valores del diccionario
persona["profesion"] = "Ingeniera"  # Agregación de key y value
del persona["edad"] # eliminación de par key, value del diccionario
```

### 3.Conjuntos

Un **conjunto** es una colección **no ordenada**, **sin elementos duplicados** y **mutable** (puede cambiarse después de su creación).

Son útiles cuando se necesita asegurar que **no haya elementos repetidos** o para realizar operaciones matemáticas como **unión**, **intersección** y **diferencia**.

La manera de crear conjuntos es utilizar la función `set` sobre iterables o utilizar paréntesis `{e1,e2,...,en}` teniendo la precaución de utilizarlo cuando el conjunto no esta vacío ya que esto `{}` crea un diccionario.

#### 3.1 Operaciones más comunes

```python
conjunto_vacio=set() # creación de set vacío
conjunto_desde_iterable=set('gato')
conjunto_desde_iterable.add('g') # inserción de elemento a set
conjunto_desde_iterable.remove('g') # eliminación de elemento del set
```

### 4. Tuplas

Una **tupla** es una colección **ordenada** e **inmutable** de elementos. A diferencia de las listas (`list`), no se pueden modificar una vez creadas.

Son útiles para representar **grupos fijos de datos**, como coordenadas, registros o retornos múltiples de funciones.

Para crear tuplas se utiliza parentesis `()`, la función `tuple` o la sintaxis comas sobre cada elemento sin paréntesis `el1,el2,el3,...,eln`

#### 4.1 Operaciones más comunes

```python
tupla1=(4,5,6) # creación de tupla utilizando paréntesis
tupla2=4,5,6  # creación de tupla utilizando solo comas
tupla3=8, # creación de tupla de un solo elemento

tupla1[0] # acceso a elementos de la tupla por índices
```

## Sentencias Iterativas

### 1.Ciclo For

El ciclo `for` es utilizando para iterar sobre secuencias de elementos ya sea listas, diccionarios, set, tuplas, cadenas y similares, permitiendo recorrer cada uno de los elementos. A diferencia de otros lenguajes, el ciclo `for` en Python permite recorrer cada elemento por defecto en vez de los índices.

La sintaxis básica es la siguiente:

```python
for variable in iterable:
    # bloque de código de contenido
```

Se utilizan adicionalmente las sentencias siguientes:

- `break`: para terminar el bucle prematuramente

- `continue`: salta a la siguiente iteración

- `else`: se ejecuta solo si el bucle terminó sin break

#### Ejemplos

Recorrido de lista por elemento y por índice:

```python
nombres = ["Ana", "Luis", "Pedro"]

for nombre in nombres:
    print(f"Hola, {nombre}")

for i in range(0,len(nombres)):
    print(f"Hola, {nombres[i]}")
```

Recorrido de diccionario:

```python
persona = {"nombre": "Ana", "edad": 30}

for clave, valor in persona.items():
    print(f"{clave} → {valor}")
```

### 2.Ciclo While

El ciclo `while` permite ejecutar **un bloque de código repetidamente mientras se cumpla una condición lógica**.

Es útil cuando **no se sabe cuántas veces se necesita repetir algo**, pero sí se sabe que debe repetirse mientras una condición sea verdadera.

```python
while condición:
    # bloque de código de contenido
```

Mientras la condición sea True, el bloque se seguirá ejecutando. Las sentencias `continue`, `break` y `else` siguen la misma lógica que las aplicadas en el ciclo `for`.

#### Ejemplos

Ciclo `while` con límite:

```python
contador = 0

while contador < 5:
print("Contador:", contador)
contador += 1
```

Ciclo `while` infinito:

```python
while True:
    print("Esto nunca termina")
```

## Sentencias Condicionales

Las **sentencias condicionales** permiten que un programa tome **decisiones** y ejecute diferentes bloques de código dependiendo de si una condición es verdadera (`True`) o falsa (`False`).

Se usan con las palabras clave `if`, `elif` y `else`.

La sintaxis básica es la siguiente:

```python
if condición:
    # Bloque si la condición es verdadera
elif otra_condición:
    # Bloque si la otra condición es verdadera
else:
    # Bloque si ninguna condición se cumple
```

### Operadores de comparación

| Operador | Significado   | Ejemplo (x = 5, y = 3) |
| -------- | ------------- | ---------------------- |
| ==       | Igual a       | x == y → False         |
| !=       | Distinto de   | x != y → True          |
| <        | Menor que     | x < y → False          |
| >        | Mayor que     | x > y → True           |
| <=       | Menor o igual | x <= y → False         |
| >=       | Mayor o igual | x >= y → True          |

### Operadores lógicos

| Operador | Significado                    | Ejemplo (x = 5)            |
| -------- | ------------------------------ | -------------------------- |
| and      | Y (todas deben ser verdaderas) | x > 3 and x < 10 → True    |
| or       | O (al menos una verdadera)     | x < 3 or x > 4 → True      |
| not      | Negación                       | not(x > 5) → True si x ≤ 5 |

### Ejemplos

```py
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

```

## Comprehensions

Las **comprehensions** son una forma concisa y elegante de **crear estructuras de datos** a partir de iterables (como listas, rangos o diccionarios) en una sola línea de código.

En lugar de usar varios `for` y `append`, es posible **expresar la lógica de creación directamente**.

Python admite comprehensions para:

- `list` → lista por comprensión
- `set` → conjunto por comprensión
- `dict` → diccionario por comprensión
- (también `generator expressions`, pero se ven aparte)

### Comprehension de Listas

La sintaxis es la siguiente cuando se filtra por condición:

```python
[expresión for elemento in iterable if condición]
```

La sintaxis es la siguiente cuando en función de una condición se debe modificar el valor considerado:

```python
[expresion_if_true if condicion else expresion_if_false for elemento in iterable]
```

#### Ejemplo

```python
cuadrados = [x**2 for x in range(5)] # creación de lista de cuadrados

pares = [x for x in range(10) if x % 2 == 0] # creación de lista de cuadrados pares
```

### Comprehension de Conjuntos

La sintaxis es la siguiente:

```python
{expresión for elemento in iterable if condición}
```

La expresión condicional es similar a la de listas.

#### Ejemplo

```python
letras = {letra for letra in "banana"} # conjunto letras solo contiene letras únicas
```

### Comprehension de Diccionarios

Para filtrar en base a una condición, la sintaxis es la siguiente:

```python
{clave: expresion_para_valor for elemento in iterable if condición_opcional}
```

Cuando en función de una condición se debe modificar el valor considerado, la sintaxis es la siguiente:

```python
{clave: valor_si_verdadero if condición else valor_si_falso for elemento in iterable}
```

#### Ejemplo

```python
clasificacion = {x: "par" if x % 2 == 0 else "impar" for x in range(6)}
```
