import pickle
class Juguete:
    nombre = ""
    precio = 0.0
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def getNombre(self):
        return self.nombre
    
#j1 = Juguete('Gary',7.99)

f = open('datos.bin', 'rb')
gary = pickle.load(f)
f.close()

print(gary.getNombre())

class Estado:
    players = Players()
    status = Status()
    life_remaining = 12
    armor = False

f = open('gamestatus.dat','wb')
e = Estado()
pickle.dumps(f,e)
f.close()