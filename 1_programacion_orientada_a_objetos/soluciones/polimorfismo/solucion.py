class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcular_bonus(self):
        return 0

class Desarrollador(Empleado):
    def calcular_bonus(self):
        return self.sueldo * 0.20

class Gerente(Empleado):
    def calcular_bonus(self):
        return self.sueldo * 0.40

def calcular_total_bonos(lista_empleados):
    total = 0
    for empleado in lista_empleados:
        total += empleado.calcular_bonus()
    return total
