import random
calificaciones=[random.randint(0,100) for _ in range(10)]
aprobados=[]
suma_total=0
for calificacion in calificaciones:
    suma_total+=calificacion
    if calificacion>=60:
        aprobados.append(calificacion)

promedio=suma_total/len(calificaciones)
print(f"El promedio de calificaciones del curso es: {promedio}. La cantidad de aprobados es: {len(aprobados)}")