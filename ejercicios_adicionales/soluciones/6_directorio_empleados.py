empleados={
    "empleado1":{
        "nombre":"Waldo",
        "edad":25
    },
    "empleado2":{
        "nombre":"Pepito",
        "edad":30
    },
    "empleado3":{
        "nombre":"Luis",
        "edad":35
    },
    "empleado4":{
        "nombre":"Ana",
        "edad":40
    },
    "empleado5":{
        "nombre":"Maria",
        "edad":45
    }
}

nombres_menores_30=[]
print("Los empleados mayores de 30 son:")
for empleado,datos in empleados.items():
    if datos["edad"]<30:
        nombres_menores_30.append(datos["nombre"])
    else:
        print(f"{datos['nombre']} es mayor de 30")

print(f"La cantidad de empleados totales es: {len(empleados)}. La cantidad de empleados menores a 30 es: {len(nombres_menores_30)}")