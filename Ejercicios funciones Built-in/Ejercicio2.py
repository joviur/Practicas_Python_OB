# Ejercicio2:
from functools import reduce
lista = [1,2,3,4,5]

def es_impar(x):
    if not x % 2 == 0:
        return x
    return False
        
filtrada = list(filter(es_impar, lista))
resultado = reduce(lambda a,b: a + b, list(filtrada))
print(resultado)