# Escribe un programa que pida una fecha (día, mes y año) e indique si es correcta

print("FECHA")

dia=int(input("Introduzca el día: "))
mes=int(input("Introduzca el mes (número): "))
ano=int(input("Introduzca el año: "))

if(mes>12 or mes<1):
    print("No ha introducido un valor de mes correcto.")
elif(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
    if(dia>31 or dia<1):
        print("No ha introducido un valor de día o de mes correcto.")
    else:
        print("Fecha váida")
elif(mes==4 or mes==6 or mes==9 or mes==11):
    if(dia>30 or dia<1):
        print("No ha introducido un valor de día o de mes correcto.")
    else:
        print("Fecha váida")
elif(mes==2):
    if(not ano % 4 and (ano % 100 or not ano % 400) and (dia<=29 and dia>0)):
        print("Fecha válida")
    elif(dia<=28 and dia>0):
        print("Fecha válida")
    else:
        print("No ha introducido un valor de día, de mes o de año correcto (tenga en cuenta que ese año puede ser o no bisiesto).")
