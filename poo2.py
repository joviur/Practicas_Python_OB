#Probando clases y herencias

class Coche:
    _estado_motor = False

    def __init__(self):
        print("Estoy en el constructor")
    
    def arrancar(self):
        self._estado_motor = True
        print("El coche arranca")

    def get_estado(self):
        return self._estado_motor
    
    def apagar(self):
        self._estado_motor = False
        print("El coche se apaga")


class hyundai(Coche):
    _asistencia_carril: True

    def arrancar(self):
        self._estado_motor = True
        print("El coche arrancaasdasd")

    def apaga_asistencia_carril(self):
        self._asistencia_carril: False
        print("Se ha apagado la asistencia de carril")

toyotaYaris = Coche()
toyotaYaris.arrancar()
print(toyotaYaris.get_estado())
toyotaYaris.apagar()
print(toyotaYaris.get_estado())

print("------- i20 -------")
i20 = hyundai()
print(i20.get_estado())
i20.arrancar()
print(i20.get_estado())
i20.apaga_asistencia_carril()

