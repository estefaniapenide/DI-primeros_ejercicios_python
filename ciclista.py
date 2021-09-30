#Un ciclista parte de una ciuadad A a las HH horas, MM minutos y SS segundos.
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#Escribir un algoritmo que determine la hora de llegada a la ciudad B

print("CICLISTA\n")

salida=input("Introduzca la hora de salida (formato HH:MM:SS): ")

hora=int(salida[0]+salida[1])
minutos=int(salida[3]+salida[4])
segundos=int(salida[6]+salida[7])

T=int(input("Introduzca el tiempo de viaje en segundos: "))

if(T>=3600):
    horasdemas=T//3600
    T=T%3600
    minutosdemas=T//60
    segundosdemas=T%60
if(T>=60 and T<3600):
    horasdemas=0
    minutosdemas=T//60
    segundosdemas=T%60
else:
    horasdemas=0
    minutosdemas=0
    segundosdemas=T

hora= hora + horasdemas
minutos = minutos + minutosdemas
segundos = segundos + segundosdemas


print("\nEl ciclista llegará a la ciudad B a las %d:%e:%f" % (hora,minutos,segundos))




   

