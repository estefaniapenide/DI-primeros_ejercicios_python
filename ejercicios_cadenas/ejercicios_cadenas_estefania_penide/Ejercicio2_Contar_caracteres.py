# Pide una cadena y un carácter por teclado(valida que sea un caracter)
# y muestra cunatas veces aparece el carácter en la cadena.
print("CONTADOR REPETICIÓN DE CARACTERES")

cadena=(str(input("\nIntroduzca una cadena: ")))

comprobacion=False
while(comprobacion==False):
    caracter=(str(input("Introduzca un caracter: ")))
    if(len(caracter)==1):
        comprobacion=True
    else:
        comprobacion=False
        print("No ha introducido un caracter")

# Si considero que por ejemplo 'J' es lo mismo que 'j', entonces paso
#tanto la cadena como el caracter todo a minúsculas para que no afecte 
#a la hora de compararlos. De lo contrario, las dos siguientes líneas de 
#código no son necesarias.
cadena=cadena.lower()
caracter=caracter.lower()

i=0
contador=0
while(i<len(cadena)):
    if(cadena[i]==caracter):
        contador=contador+1    
    i=i+1

print("\nNúmero de veces que aparece '"+caracter+"' en '"+cadena+"': %s"%(contador))