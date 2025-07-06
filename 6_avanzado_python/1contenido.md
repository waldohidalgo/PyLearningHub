# Python Avanzado

El objetivo de este capítulo es dar una introducción en el uso avanzado del lenguaje Python, enfocándose en su naturaleza multiparadigma, el aprovechamiento de bibliotecas estándar y la aplicación práctica en tareas como análisis de datos y diseño de software más robusto.

## Tabla de Contenidos

- [Python Avanzado](#python-avanzado)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [1.Python como lenguaje multiparadigma](#1python-como-lenguaje-multiparadigma)
    - [Programación imperativa](#programación-imperativa)
    - [Programación funcional](#programación-funcional)
    - [Programación orientada a objetos](#programación-orientada-a-objetos)
  - [2.Uso avanzado de la librería estándar](#2uso-avanzado-de-la-librería-estándar)
    - [Manejo de archivos y sistema](#manejo-de-archivos-y-sistema)
    - [Fechas y tiempo](#fechas-y-tiempo)
    - [Colecciones y estructuras de datos](#colecciones-y-estructuras-de-datos)
    - [Matemáticas y estadísticas](#matemáticas-y-estadísticas)
    - [Iteradores y programación funcional](#iteradores-y-programación-funcional)
    - [Entrada/salida y formatos de datos](#entradasalida-y-formatos-de-datos)
    - [Red y web](#red-y-web)
    - [Pruebas, depuración y logging](#pruebas-depuración-y-logging)
    - [Sistema y desarrollo](#sistema-y-desarrollo)
    - [Seguridad y cifrado básico](#seguridad-y-cifrado-básico)

## 1.Python como lenguaje multiparadigma

Python permite mezclar varios estilos de programación de forma natural. Los tres principales paradigmas que se combinan son:

### Programación imperativa

Se caracteriza por una secuencia de instrucciones explícitas que modifican el estado del programa. Por ejemplo:

```py
datos = [1, 2, 3]
dobles = []
for x in datos:
    dobles.append(x * 2)
```

### Programación funcional

Uso de funciones puras, expresiones sin efectos secundarios y herramientas como **map**, **filter**, **reduce**, **lambda**.

Por ejemplo:

```py
dobles = list(map(lambda x: x * 2, [1, 2, 3]))
```

El módulo **functools** proporciona funciones de orden superior permitiendo aplicar principios de la programación funcional

```py
from functools import reduce

suma = reduce(lambda x, y: x + y, [1, 2, 3])
print(suma)
```

En Python, las funciones son "ciudadanos de primera clase", lo que significa que pueden:

- Ser asignadas a variables.

- Ser pasadas como argumentos a otras funciones.

- Ser retornadas como resultado de otras funciones.

Una función de orden superior es simplemente una función que hace una o ambas de estas cosas:

- Toma una o más funciones como argumentos.

- Devuelve una función como resultado.

### Programación orientada a objetos

Este paradigma permite organizar el código en clases que encapsulan datos y comportamientos. En el primer capítulo de este tutorial se dan mayores explicaciones, ejemplos y ejercicios: [link](../1_programacion_orientada_a_objetos/1contenido.md)

## 2.Uso avanzado de la librería estándar

Python incluye una poderosa librería estándar built-in, ideal para tareas avanzadas sin necesidad de instalar librerías externas. A continuación se muestra un listado de los módulos más relevantes junto con una descripción:

### Manejo de archivos y sistema

| Módulo     | Descripción                                                          |
| ---------- | -------------------------------------------------------------------- |
| `os`       | Interfaz con el sistema operativo (rutas, archivos, procesos, etc.). |
| `pathlib`  | Manejo moderno y orientado a objetos de rutas de archivos.           |
| `shutil`   | Operaciones de alto nivel sobre archivos y carpetas.                 |
| `glob`     | Búsqueda de archivos mediante patrones (`*.txt`, etc.).              |
| `tempfile` | Creación de archivos y carpetas temporales.                          |

### Fechas y tiempo

| Módulo     | Descripción                                               |
| ---------- | --------------------------------------------------------- |
| `datetime` | Manipulación de fechas y tiempos.                         |
| `time`     | Funciones relacionadas con el tiempo y demoras (`sleep`). |
| `calendar` | Generación de calendarios y utilidades para fechas.       |

### Colecciones y estructuras de datos

| Módulo        | Descripción                                                              |
| ------------- | ------------------------------------------------------------------------ |
| `collections` | Contenedores especializados como `Counter`, `deque`, `defaultdict`, etc. |
| `array`       | Arreglos eficientes de datos numéricos.                                  |
| `heapq`       | Implementación de colas de prioridad (heaps).                            |
| `bisect`      | Algoritmos de búsqueda binaria y mantenimiento de listas ordenadas.      |

### Matemáticas y estadísticas

| Módulo       | Descripción                                                      |
| ------------ | ---------------------------------------------------------------- |
| `math`       | Funciones matemáticas estándar (trigonometría, log, raíz, etc.). |
| `statistics` | Cálculo de media, mediana, varianza y desviación estándar.       |
| `random`     | Generación de números aleatorios y funciones relacionadas.       |
| `decimal`    | Aritmética decimal de precisión arbitraria.                      |
| `fractions`  | Aritmética exacta con fracciones.                                |

### Iteradores y programación funcional

| Módulo      | Descripción                                                             |
| ----------- | ----------------------------------------------------------------------- |
| `itertools` | Herramientas eficientes para iteración (`combinations`, `cycle`, etc.). |
| `functools` | Funciones de orden superior (`reduce`, `lru_cache`, decoradores, etc.). |
| `operator`  | Funciones que representan operadores (`add`, `itemgetter`, etc.).       |

### Entrada/salida y formatos de datos

| Módulo   | Descripción                                                  |
| -------- | ------------------------------------------------------------ |
| `csv`    | Lectura y escritura de archivos en formato CSV.              |
| `json`   | Serialización y deserialización en formato JSON.             |
| `pickle` | Serialización de objetos Python en binario.                  |
| `io`     | Flujos de entrada/salida avanzados (archivos, memoria, etc). |

### Red y web

| Módulo   | Descripción                                           |
| -------- | ----------------------------------------------------- |
| `urllib` | Cliente HTTP, manejo de URLs y descarga de contenido. |
| `http`   | Herramientas para crear o analizar servidores HTTP.   |
| `socket` | Comunicación en red de bajo nivel (TCP/UDP).          |

### Pruebas, depuración y logging

| Módulo      | Descripción                                             |
| ----------- | ------------------------------------------------------- |
| `unittest`  | Framework para escribir y ejecutar tests automatizados. |
| `doctest`   | Pruebas basadas en ejemplos dentro de la documentación. |
| `logging`   | Sistema flexible de registro de eventos y errores.      |
| `traceback` | Análisis y personalización de rastreos de errores.      |
| `pdb`       | Depurador interactivo de código Python.                 |

### Sistema y desarrollo

| Módulo       | Descripción                                                      |
| ------------ | ---------------------------------------------------------------- |
| `argparse`   | Análisis de argumentos desde la línea de comandos (CLI).         |
| `sys`        | Interacción con el intérprete (argumentos, stdin, stdout, etc.). |
| `subprocess` | Ejecución de comandos externos y manejo de su entrada/salida.    |
| `platform`   | Información sobre el sistema operativo, arquitectura, etc.       |

### Seguridad y cifrado básico

| Módulo    | Descripción                                               |
| --------- | --------------------------------------------------------- |
| `hashlib` | Funciones hash como MD5, SHA1, SHA256, etc.               |
| `secrets` | Generación segura de contraseñas o tokens aleatorios.     |
| `uuid`    | Generación de identificadores únicos universales (UUIDs). |
