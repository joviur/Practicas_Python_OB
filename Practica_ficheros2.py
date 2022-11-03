lista = [
    'una linea',
    'dos lineas',
    'tres lineas'
]

def escribe(file,list):
    f = open(file,'w')
    for linea in list:
        if not linea.endswith('/n'):
            linea += '\n'
            
        f.write(linea)
    
    f.close()

def muestra(file):
    f = open(file,'r')
    print(f.read())
    
    f.close()
    
escribe('mifichero.txt',lista)
muestra('mifichero.txt')