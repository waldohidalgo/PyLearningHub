# Tabla de Contenido

- [Tabla de Contenido](#tabla-de-contenido)
- [Clases en Python](#clases-en-python)
  - [1.Creación de Clase](#1creación-de-clase)
    - [Ejemplo: Creacion de Clase e instanciación de objeto](#ejemplo-creacion-de-clase-e-instanciación-de-objeto)
  - [2.Encapsulamiento](#2encapsulamiento)
  - [3.Herencia](#3herencia)
  - [4.Polimorfismo](#4polimorfismo)

# Clases en Python

Las clases son una forma de agrupar datos y funcionalidades en una sola entidad desde la cual es posible crear un nuevo tipo de objeto a partir de la creación de **instancias** de dicho tipo. En Python, las clases se definen utilizando la palabra clave `class`. Dentro de la clase se definen los atributos(datos) y métodos(funcionalidad) que cada instancia de la clase tendrá. Los atributos son variables que se crean dentro de la clase y pueden ser accedidas por los métodos de la clase. Los métodos son funciones que se definen dentro de la clase y que pueden acceder y modificar los atributos de la clase.

La ventaja principal de utilizar clases es que permiten organizar el código de una forma más clara y estructurada, lo que facilita la comprensión y el mantenimiento del código. Además, permiten crear objetos que tengan comportamientos y atributos similares, lo que facilita la reutilización del código.

En esta sección, vamos a ver cómo se definen las clases en Python, cómo se crean objetos a partir de las clases, y cómo se pueden utilizar los métodos y atributos de las clases para crear objetos que tengan comportamientos y atributos específicos. Los conceptos fundamentales de esta sección son: Clases, Objetos, Atributos, Métodos, Palabra Clave Self y el método constructor `__init__`.

## 1.Creación de Clase

Para crear una clase se utiliza la palabra clave `class`, seguida del nombre de la clase con la primera letra en mayúscula (por convención). Dentro de la clase, se puede definir un constructor usando el método especial `__init__`, que se ejecuta automáticamente cuando se crea un nuevo objeto.

A continuación, se muestra la estructura fundamental para crear una clase:

```py
class NombreDeLaClase:
    atributo_de_clase=value1
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2

    def metodo(self):
        pass
```

Donde:

- `self`: Hace referencia al propio objeto. Se usa para acceder a los atributos y métodos del objeto dentro de la clase.
- `__init__`: Es un método especial llamado constructor. Se ejecuta automáticamente y de modo ímplicito al crear una instancia (objeto) de la clase.
- atributo1, atributo2: Son variables asociadas a cada objeto creado.
- atributo_de_clase: Es una atributo compartido por cada instancia de la clase

Para crear una instancia de una clase, es decir, un objeto que utiliza la clase como plantilla es necesario utilizar el nombre de la clase seguido de valores para cada parámetro del método constructor `__init__`. Para la estructura anterior, el código de creación de un objeto es el siguiente:

```py
objeto = NombreDeLaClase(argumento1,argumento2)
```

### Ejemplo: Creacion de Clase e instanciación de objeto

El siguiente código muestra la creación de la clase **Persona** en la cual cada instancia de la clase debe tener dos atributos: **nombre** y **edad**. Además, se crea el método **saludar** que tiene como acción mostrar en consola un mensaje:

```py
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
```

Lo siguiente muestra como crear objetos con valores especificos para cada parámetro:

```py
persona1 = Persona("Ana", 28)
persona2 = Persona("Luis", 35)

persona1.saludar()
persona2.saludar()
```

## 2.Encapsulamiento

El encapsulamiento es uno de los **principios** fundamentales de la Programación Orientada a Objetos. Su propósito es ocultar los detalles internos de una clase y proteger los datos para que no sean modificados directamente desde fuera de la clase. El encapsulamiento permite:

- Controlar el acceso a los atributos.

- Evita que los objetos queden en un estado inconsistente al controlar la lógica de manipulación

Python no tiene modificadores de acceso estrictos como otros lenguajes (por ejemplo, private, protected, public en Java), pero usa convenciones de nombre para simular esos niveles:

| Notación     | Tipo de acceso | Uso típico                                                                   |
| ------------ | -------------- | ---------------------------------------------------------------------------- |
| variable     | público        | Puede accederse desde fuera de la clase                                      |
| `_variable`  | Protegido      | Solo debe usarse dentro de la clase o subclases (convención, no obligatorio) |
| `__variable` | Privado        | No puede accederse directamente desde fuera de la clase                      |

A continuación, se muestra un ejemplo de acceso público al atributo saldo permitiendo su modificación sin control:

```py
class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

cuenta1 = Cuenta(1000)
cuenta1.saldo = -5000
```

El siguiente ejemplo hace uso de la encapsulación para controlar la manipulación de atributos:

```py
class Cuenta:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes o monto inválido.")

    def obtener_saldo(self):
        return self.__saldo

cuenta = Cuenta(1000)
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.obtener_saldo())
```

El `print` del código anterior muestra 1300. Si se intenta acceder al atributo privado `__saldo`, se muestra un error de tipo `AttributeError`:

```py
print(cuenta.__saldo) # AttributeError: 'Cuenta' object has no attribute '__saldo'
```

## 3.Herencia

La herencia permite crear una clase nueva (subclase o clase hija) que hereda los atributos y métodos de otra clase (superclase o clase padre), y opcionalmente puede extenderlos o modificarlos. Permitiendo realizar:

- Reutilización de código.

- Organización jerárquica.

- Flexibilidad para personalizar comportamientos.

La sintaxis básica de herencia es la siguiente:

```py
class ClasePadre:
    # atributos y métodos de la clase padre
    pass

class ClaseHija(ClasePadre):
    # hereda todo de ClasePadre
    # puede agregar o sobreescribir cosas
    pass

```

En la herencia, el método `super()` permite llamar a métodos de la clase padre desde una subclase, sin tener que escribir directamente el nombre de la clase base. Es utilizado para inicialiar atributos base o extender métodos. El siguiente ejemplo muestra el uso del método `super`:

```py
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def informacion(self):
        return f"Empleado: {self.nombre} - Sueldo: {self.sueldo}"

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def informacion(self):
        return f"Gerente: {self.nombre} - Sueldo: {self.sueldo} - Departamento: {self.departamento}"

```

El Gerente hereda de la clase empleado los atributos `nombre` y `sueldo` y sobreescribe el método `informacion`.

## 4.Polimorfismo

Polimorfismo (del griego "muchas formas") permite que múltiples clases diferentes respondan a los mismos métodos, aunque cada una lo haga a su manera. A continuación se definen multiples clases que implementan un método llamado `descripcion` pero difieren en su implementación:

```py
class Animal:
    def descripcion(self):
        return "Este es un animal."

class Perro(Animal):
    def descripcion(self):
        return "Este es un perro."

class Gato(Animal):
    def descripcion(self):
        return "Este es un gato."
```
