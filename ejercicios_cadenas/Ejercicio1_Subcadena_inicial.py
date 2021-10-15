# Programa que comprueba si una cadena leída por teclado 
# comienza por una subcadena introducida por teclado.
print("COMPROBACIÓN SUBCADENA")

cadena = (str(input("Introduzca una cadena: ")))
subcadena=(str(input("Introduzca el inicio de la cadena anterior: ")))

long =len(subcadena)

if(cadena[0:long]==subcadena):
    print("La primera cadena comienza por la subcadena introducida por teclado.")
else:
    print("La primera cadena NO comienza por la subcadena introducida por teclado.")

