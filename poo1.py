class coche:
    _arrancar = False

    def arrancar(self):
        self._arrancar = True
    
    def apagar(self):
        self._arrancar = False

i20 = coche()

print(i20._arrancar)
i20.arrancar()
i20.apagar()
print(i20._arrancar)
