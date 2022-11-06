### Practicas con funciones Built-In ###
## Funcion filter()
numeros = [1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x % 2 == 0:
        return True
    return False
resultado = filter(mifuncion, numeros)
print(list(resultado))

#Lo mismo con una función lambda o anónima

resultado = filter(lambda n: n % 2 == 0, numeros)
print(list(resultado))

#Otra prueba con filter

resultado = filter(lambda x: x.startswith('p'), ['pepe', 'pepito', 'juan'])
print(list(resultado))

## Funcion map()

def cuadrado(x):
    return x*x

lista = (1,2,3,4,5,6,7,8,9,10)
resultado = map(cuadrado,lista)
print(list(resultado))

#Lo mismo con una lamda

resultado = map(lambda x: x*x, lista)
print(list(resultado))

## Funcion reduce() NOTA: Hay que importar al funcion
from functools import reduce

def suma(a,b):
    return a + b

res = reduce(suma,[1,2,3,4,5,6,7,8,9])
print(res)

# Lo mismo con una lambda

res = reduce(lambda a,b: a+b,[1,2,3,4,5,6,7,8,9])
print(res)

## Zip

cursos = ('Java', 'Python', 'Git')
asistentes = (15,20,4)

demo = zip(cursos, asistentes)
print(list(demo))

## All y Any
listaA = [1==1, 2==2, 3==4]
res = all(listaA)
print(res)