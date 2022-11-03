import pickle
class Vehiculo:
    ruedas = None
    puertas = None
    caballos = None
    
    _estado = False
    
    def __init__(self,ruedas, puertas, caballos):
        self.ruedas = ruedas
        self.puertas = puertas
        self.caballos = caballos

    def arrancar(self):
        self._estado = True
        print("Se ha arrancado el vehiculo")
    
    def parar(self):
        self._estado = False
        print("Se ha apagado el vehiculo")
        
hyundai = Vehiculo(4,5,100)

f = open('estado_vehiculos.bin','wb')
pickle.dump(hyundai, f)
f.close()

coche = pickle.load(open('estado_vehiculos.bin','rb'))
print(coche.caballos)
