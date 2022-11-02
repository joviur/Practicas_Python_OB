import time

tiempo = time.localtime()
hora = tiempo[3]
minuto = tiempo[4]

def alarma(hora_limite):
    print("Son las: ",hora,":", minuto, sep="")
    if hora <= hora_limite:
        hora_restante = hora_limite-hora
        min_restante = 60-minuto
        print("Queda:", hora_restante, "horas y", min_restante,"minutos para salir de trabajar")
    else:
        print("¡Es hora de ir a casa!")

alarma(17)