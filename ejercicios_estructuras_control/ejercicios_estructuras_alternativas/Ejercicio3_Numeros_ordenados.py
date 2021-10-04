# Algoritmo que te pida tres número y los muestre ordenados (de mayor a menor)

#Corregir!!!

print("NÚMEROS ORDENADOS")

num1=float(input("Introduzca un número: "))
num2=float(input("Introduzca otro número: "))
num3=float(input("Introduzca otro número: "))

if(num1>num2):
    if(num2 > num3):
        print("Números orenados: %d > %s > %r" % (num1,num2,num3))
    if(num2<num3):
        print("Números orenados: %d > %s > %r" % (num1,num3,num2))
    else:
        print("Números orenados: %d es el mayor y %s y %r son iguales" % (num1,num2,num3))
elif(num2>num1):
    if(num1 > num3):
        print("Números orenados: %d > %s > %r" % (num2,num1,num3))
    if(num1<num3):
        print("Números orenados: %d > %s > %r" % (num2,num3,num1))
    else:
        print("Números orenados: %d es el mayor y %s y %r son iguales" % (num2,num1,num3))
elif(num3>num1):
    if(num1 > num2):
        print("Números orenados: %d > %s > %r" % (num3,num1,num2))
    if(num1<num2):
        print("Números orenados: %d > %s > %r" % (num3,num2,num1))
    else:
        print("Números orenados: %d es el mayor y %s y %r son iguales" % (num3,num2,num1))
elif (num1==num2):
    if(num2==num3):
        print("Todos los números son iguales.")
    elif(num2>num3):
        print("Números orenados: %d y %s son iguales y %r es el menor" % (num1,num2,num3))
elif (num2==num3):
    if(num3>num1):
        print("Números orenados: %d y %s son iguales y %r es el menor" % (num2,num3,num1))
