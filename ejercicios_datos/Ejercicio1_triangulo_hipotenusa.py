#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa
import math

print("Cáculo de la hipotenusa de un triángulo rectángulo")

a=float(input("Cateto(cm): "))
b=float(input("Cateto(cm): "))

h=math.sqrt(pow(a,2)+pow(b,2))

print("La hipostenusa del triángulo mide %d cm" % (h))