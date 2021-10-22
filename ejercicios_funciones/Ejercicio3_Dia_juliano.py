# Un día juliano a una fecha es un número entero que indica los días
# que han transcurrido desde el 1 de enero del año indicado.
# Queremos crear un programa principal que al introducir
# una fecha nos diga el día juliano que corresponde.
# Para ello se harán las siguientes subrutinas:
# LeerFecha: lee por teclado una fecha (día, mes, año)
# DiaDelMes: recibe un mes y un año y nos dice los días de ese mes en ese año.
# EsBisisesto: recibe un año y nos dice si es bisisesto o no
# Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano

print("DÍA JULIANO\n")

error="La fecha introducida no es válida.\n"
errorTipo="ERROR. Debe introducir un número entero."

def LeerFecha():
    d=False
    m=False
    y=False

    while(not d or not m or not y):
        while(True):
            try:
                dia=int(input("Día: "))
                if(dia<1):
                    d=False
                else:
                    d=True
                break
            except ValueError:
                print(errorTipo)
        while(True):
            try:
                mes=int(input("Mes: "))
                if(mes<1 and mes>12):
                    m=False
                else:
                    m=True
                break
            except ValueError:
                print(errorTipo)
        while(True):
            try:
                year=int(input("Año: "))
                if(DiaDelMes(mes,year)<dia):
                    y=False
                else:
                    y=True  
                break
            except ValueError:
                print(errorTipo) 

        if(not d or not m or not y):
             print(error)

    return dia,mes,year
        

def EsBisiesto(year):
    bisiesto=False
    if(not year % 4 and (year % 100 or not year % 400)):
        bisisesto=True
    else:
        bisisesto=False
    return bisisesto

def DiaDelMes(mes,year):
    dias=0
    if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        dias=31
    elif(mes==4 or mes==6 or mes==9 or mes==11):
        dias=30
    elif(EsBisiesto(year) and mes==2):
        dias=29
    elif(not EsBisiesto(year) and mes==2):
        dias=28
    return dias

def Calcular_Dia_Juliano(LeerFecha):

    diaJuliano=0

    dia=LeerFecha[0]
    mes=LeerFecha[1]
    year=LeerFecha[2]

    if(mes==1):
        diaJuliano=dia
    else:
        i=0
        while(i<(mes)):
            diaJuliano=diaJuliano+DiaDelMes(i,year)
            i=i+1
        diaJuliano=diaJuliano+dia
        
    return diaJuliano

print("\nDía Juliano:",Calcular_Dia_Juliano(LeerFecha()))

