# Programa que comprueba si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado
print("SUBCADENA EN CADENA")

cadena=str(input("Introduzca una cadena: "))
subcadena=str(input("Introduzca una subcadena contenida en la cadena anterior: "))

# Si considero que por ejemplo 'J' es lo mismo que 'j', entonces paso
#tanto la cadena como la subcadena todo a minúsculas para que no afecte 
#a la hora de compararlos. De lo contrario, las dos siguientes líneas de 
#código no son necesarias.
cadena.lower()
subcadena.lower()

if(subcadena in cadena):
    print("La subcadena pertenece a la cadena anterior.")
else:
    print("La subcadena NO pertenece a la cadena anterior.")