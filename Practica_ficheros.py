#Practica de lectura de ficheros, métodos de cadenas y buenas practicas.
#Hasta que en Windows no exista el fichero /etc/passwd, este script no funciona en Windows.
def main():
    usuarios = listarUsuarios()
    for usuario in usuarios:
        print(f'Usuario: {usuario}')

def listarUsuarios():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()
    resultado =[]
    for linea in datos:
        #Lo siguiente es solo para sistemas MacOS
        if linea[0] == '#' or linea[0] == '_':
            continue
        partes = linea.split(":")
        resultado.append(partes[0])
        # print(linea)
    return resultado

if __name__ == '__main__':
    main()

listarUsuarios()