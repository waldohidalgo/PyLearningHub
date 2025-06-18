# Actividades Propuestas

## Tabla de Contenido

- [Actividades Propuestas](#actividades-propuestas)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Encapsulamiento](#encapsulamiento)

## Encapsulamiento

En la carpeta **encapsulamiento** en esta misma ruta, se encuentra el archivo llamado **encapsulamiento** en el cual deberás crear una clase **Producto** que tenga un atributo privado `__precio`. Implementa métodos para:

- Establecer el precio (debe ser llamado set_precio), solo si es mayor que cero.

- Obtener el precio (debe ser llamado get_precio).

Ejemplo de implementación esperada:

```py
p = Producto()
p.set_precio(1500)
print(p.get_precio())  # Debe mostrar 1500

p.set_precio(-200)     # No debe modificar el precio
```

Una vez hayas creado la clase y sus métodos, deberás ejecutar los test unitarios para validar correctamente la implementación. En la consola de comandos deberás ejecutar el siguiente comando posicionado en dicha ruta:

```
py test_encapsulamiento.py encapsulamiento
```

Una vez hayas realizado la actividad puedes visualizar una posible solución en el archivo ubicado en esta ruta: [`1_programacion_orientada_a_objetos/soluciones/encapsulamiento/encapsulamiento_solucion.py`](./soluciones/encapsulamiento/encapsulamiento_solucion.py)
