# Algoritmo que pida un número y diga si es positivo, negativo o 0

print("NÚMERO POSITIVO, NEGATIVO O CERO")

num=float(input("Introduzca un número: "))

if num==0:
    print("El número introducido es cero")
elif num>0:
    print("El número introducido es positivo")
else:
    print("El número introducido es negativo")