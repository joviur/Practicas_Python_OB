#Prueba
import sqlite3
import getpass
import logging

def main():
    
    def verifica(username, password): #Esta funcion la utiliza login()
        conn = sqlite3.connect('./miaplicacion.db')
        cursor = conn.cursor()
        query = f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'
        rows = cursor.execute(query)
        data = rows.fetchone()
        cursor.close()
        conn.close()
        if data:
            return True
        else:
            return False

    def login():
        username = input("Nombre de usuario: ")
        password = getpass.getpass("Contraseña: ")
        
        if verifica(username, password):
            print("¡Login Correcto!")
        else:
            logging.error("¡Login Incorrecto!")

    def crear_usuario(id, nombre, contrasena):
        conn = sqlite3.connect('./miaplicacion.db')
        cursor = conn.cursor()
        query = '''INSERT INTO users(id, username, password) VALUES(?, ?, ?)''' #De esta forma es mas seguro
        print(query)
        rows = cursor.execute(query, (id, nombre, contrasena))
        print(type(rows))
        cursor.close()
        conn.commit() #Muy importante commitear cuando se hace INSERT, UPDATE o DELETE
        conn.close()

    opcion = input('¿Que deseas? \n1.Login\n2.Crear usuario\n ')
    if opcion == '1':
        login()
    elif opcion == '2':
        print('# Asistente creación de usuarios #')
        id = input('Introduce el ID deseado: ')
        nombre = input('Introduce el nombre deseado: ')
        contrasena = input('Introduce la contraseña deseada: ')
        
        crear_usuario(id,nombre, contrasena)
    else:
        main()

if __name__ == "__main__":
    main()
    

    




