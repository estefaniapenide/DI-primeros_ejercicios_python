#Un ciclista parte de una ciuadad A a las HH horas, MM minutos y SS segundos.
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#Escribir un algoritmo que determine la hora de llegada a la ciudad B

print("CICLISTA\n")

salida=input("Introduzca la hora de salida (formato HH:MM:SS): ")

hora=int(salida[0]+salida[1])
minutos=int(salida[3]+salida[4])
segundos=int(salida[6]+salida[7])


if(hora>24 or minutos > 60 or segundos > 60):
    print("No ha introducido un formato de hora válido")
else: 

    horasalida=hora*3600+minutos*60+segundos

    T=int(input("Introduzca el tiempo de viaje en segundos: "))

    horallegada=horasalida+T

    hora = horallegada//3600 
    minutos= (horallegada % 3600) // 60 
    segundos =((horallegada % 3600) % 60) 

    if(hora>24):
        dia = hora // 24
        hora=hora%24
    
        if(dia==1):
            print("\nEl ciclista llegará a la ciudad B al día siguiente a las ",hora,":",minutos,":",segundos)
        else:
            print("\nEl ciclista llegará a la ciudad B",dia,"días después a las ",hora,":",minutos,":",segundos)
    else:
        print("\nEl ciclista llegará a la ciudad B a las ",hora,":",minutos,":",segundos)