print("Calculadora de IMC")
peso = float(input("Introduce tu peso (en kilos)..."))
altura = float(input("Introduce tu altura (en metros)..."))
imc = round(peso / altura**2,2)
print('Tu Incide de Masa Corporal es: ' + str(imc))