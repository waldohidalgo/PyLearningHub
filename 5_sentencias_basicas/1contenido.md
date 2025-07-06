# Sentencias Básicas

## Tabla de Contenidos

- [Sentencias Básicas](#sentencias-básicas)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Introduccion](#introduccion)
  - [1. Asignación de variables](#1-asignación-de-variables)
  - [2. Entrada y salida de datos](#2-entrada-y-salida-de-datos)
  - [3. Condicionales](#3-condicionales)
  - [4. Bucles](#4-bucles)
    - [Bucle While](#bucle-while)
    - [Bucle For](#bucle-for)
  - [5. Operadores en Python](#5-operadores-en-python)
    - [Operadores Aritméticos](#operadores-aritméticos)
    - [Operadores de Comparación](#operadores-de-comparación)
    - [Operadores Lógicos](#operadores-lógicos)

## Introduccion

Este capítulo introduce los fundamentos del lenguaje Python que permiten construir programas sencillos pero funcionales. Se abordan conceptos esenciales como la **asignación de variables**, **estructuras condicionales**, **bucles**, **operadores** y **entrada/salida** de datos en consola.

## 1. Asignación de variables

En Python, una variable se crea automáticamente al asignarle un valor utilizando el operador =. A continuación se muestran algunos ejemplos:

```py
nombre = "Ana"
edad = 25
precio = 19.99
```

Las variables no necesitan ser declaradas previamente ni poseer algún tipo explicito debido que los tipos son dinámicos e inferidos en tiempo de ejecución.

## 2. Entrada y salida de datos

Para ingresar información por consola se utiliza la función `input` la cual retorna un string. Por ejemplo:

```py
nombre = input("¿Cómo te llamas? ")
```

Para mostrar información por consola se utiliza la función `print`. Por ejemplo:

```py
print("Hola mundo")
print("El resultado es", 42)
```

## 3. Condicionales

Sentencias que permiten ejecutar diferentes bloques de código dependiendo de una condición. La sintaxis es la siguiente:

```py
if condición:
    # bloque si la condición es verdadera
elif otra_condición:
    # bloque si la otra condición es verdadera
else:
    # bloque si ninguna condición se cumple
```

A continuación, se muestra un ejemplo:

```py
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## 4. Bucles

### Bucle While

Repite un bloque de código mientras una condición sea verdadera. El siguiente ejemplo muestra en consola la variable contador desde su valor inicial 0 hasta que el contador es 4, cuando llega a 5, la condición se evalua a falso y se termina de ejecutar el bucle:

```py
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Bucle For

Permite recorrer elementos de una secuencia (como una lista, cadena o rango). A continuación, se muestran dos ejemplos, el primer ejemplo recorre cada caracter de la cadena y el segundo ejemplo recorre una secuencia de elementos desde 0 a 2:

```py
for letra in "Python":
    print(letra)
```

```py
for i in range(3):
    print(f"Iteración {i}")
```

## 5. Operadores en Python

A continuación, se muestra una lista de los operadores aritméticos, de comparación y lógicos:

### Operadores Aritméticos

| Operador | Descripción       | Ejemplo  |
| -------- | ----------------- | -------- |
| +        | Suma              | a + b    |
| -        | Resta             | a - b    |
| \*       | Multiplicación    | a \* b   |
| /        | División flotante | a / b    |
| //       | División entera   | a // b   |
| %        | Módulo            | a % b    |
| \*\*     | Potencia          | a \*\* b |

### Operadores de Comparación

Estos operadores retornan un valor booleano:

| Operador | Significado       |
| -------- | ----------------- |
| ==       | Igual a           |
| !=       | Distinto de       |
| >        | Mayor que         |
| <        | Menor que         |
| >=       | Mayor o igual que |
| <=       | Menor o igual que |

### Operadores Lógicos

| Operador | Significado |
| -------- | ----------- |
| and      | Y lógico    |
| or       | O lógico    |
| not      | Negación    |
