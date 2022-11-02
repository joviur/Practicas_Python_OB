
from tkinter.messagebox import NO


class Vehiculo():
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self, velocidad, cilindrada):
        print("Vehiculo creado")
        self.velocidad = velocidad
        self.cilindrada = cilindrada

hyundai = Coche(150, 1200)

print(hyundai)