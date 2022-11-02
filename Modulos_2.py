import time

tiempo = time.localtime()
hora = tiempo[3]
minuto = tiempo[4]

def alarma():
    print("Son las: ",hora,":", minuto, sep="")
    if hora <= 19:
        hora_restante = 19-hora
        min_restante = 60-minuto
        print("Queda:", hora_restante, "horas y", min_restante,"minutos para salir de trabajar")
    else:
        print("¡Es hora de ir a casa!")

alarma()