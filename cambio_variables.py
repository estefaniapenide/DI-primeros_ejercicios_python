#Dadas dos variables numéricas A y B, que el uusario debe teclear, se pide realizar un algoritmo que intercambie los valores
#de ambas varariables y muestre cuanto vales al final las dos variables

print("INTERCAMBIO DE VARIABLES\n")

a=float(input("Introduzca la variable A: "))
b=float(input("Introduzca la variable B: "))

#También podría haber hecho a,b=b,a


c=a
a=b
b=c

print("\nLa variable A ahora vale %s" % (a))
print("La variable B ahora vale %d" % (b))