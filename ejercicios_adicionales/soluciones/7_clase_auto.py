class Auto:
    ESTADOS = ["Detenido", "Circulando", "Estacionado", "Dañado"]

    def __init__(self, color, peso, tamaño, alto, largo, cantidad_ruedas, cantidad_puertas, tipo):
        self.color = color
        self.peso = peso
        self.tamaño = tamaño
        self.alto = alto
        self.largo = largo
        self.cantidad_ruedas = cantidad_ruedas
        self.cantidad_puertas = cantidad_puertas
        self.tipo = tipo
        self.estado = Auto.ESTADOS[0]  

    def __str__(self):
        return (f"Auto de tipo {self.tipo} ({self.color}), actualmente {self.estado}.\n"
                f"Características: Peso={self.peso}kg, Alto={self.alto}m, Largo={self.largo}m, "
                f"Ruedas={self.cantidad_ruedas}, Puertas={self.cantidad_puertas}.")

    def arrancar(self):
        if self.estado == "Detenido" or self.estado == "Estacionado":
            self.estado = "Circulando"
            print(f"El auto {self.color} ha arrancado y ahora está {self.estado}.")
        elif self.estado == "Dañado":
            print(f"El auto {self.color} está dañado, no puede arrancar.")
        else:
            print(f"El auto {self.color} ya está {self.estado}.")

    def frenar(self):
        if self.estado == "Circulando":
            self.estado = "Detenido"
            print(f"El auto {self.color} ha frenado y ahora está {self.estado}.")
        else:
            print(f"El auto {self.color} no está circulando para frenar. Estado actual: {self.estado}.")

    def acelerar(self):
        if self.estado == "Circulando":
            print(f"El auto {self.color} está acelerando.")
        else:
            print(f"El auto {self.color} no puede acelerar, su estado es {self.estado}.")

    def girar(self, direccion):
        if self.estado == "Circulando":
            print(f"El auto {self.color} está girando a la {direccion}.")
        else:
            print(f"El auto {self.color} no puede girar, su estado es {self.estado}.")

    def estacionar(self):
        if self.estado == "Detenido" or self.estado == "Circulando":
            self.estado = "Estacionado"
            print(f"El auto {self.color} se ha estacionado y ahora está {self.estado}.")
        else:
            print(f"El auto {self.color} ya está {self.estado} o no puede estacionarse en este estado.")

    def dañar(self):
        if self.estado != "Dañado":
            self.estado = "Dañado"
            print(f"El auto {self.color} ha sido dañado y ahora está {self.estado}.")
        else:
            print(f"El auto {self.color} ya estaba {self.estado}.")

    def reparar(self):
        if self.estado == "Dañado":
            self.estado = "Detenido"
            print(f"El auto {self.color} ha sido reparado y ahora está {self.estado}.")
        else:
            print(f"El auto {self.color} no necesita reparación, su estado es {self.estado}.")



if __name__ == "__main__":
    auto1 = Auto("Negro", 1500, "mediano",1.4,4.5,4, 4, "sedán")
    print(auto1)

    print("Prueba de comportamiento:")
    auto1.acelerar() 
    auto1.arrancar()
    auto1.acelerar()
    auto1.girar("derecha")
    auto1.frenar()
    auto1.estacionar()
    auto1.arrancar()
    auto1.dañar()
    auto1.arrancar() 
    auto1.reparar()
    auto1.arrancar() 
