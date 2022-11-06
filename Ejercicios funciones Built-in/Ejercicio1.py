#Ejercicio 1:
print('### Sorter de paises ###')
paises = input('Introduce tus paises separados por comas (,) :').casefold()

def ordenar_paises(paises):
    lista = paises.split(',')
    ordenados = []
    for items in lista:
        j = items.replace(' ', '')
        ordenados.append(j)
    ordenados = set(ordenados)
    print(ordenados) 
        
ordenar_paises(paises)