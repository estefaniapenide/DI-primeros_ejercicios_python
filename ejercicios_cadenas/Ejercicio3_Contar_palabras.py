# Contar las palabras de una frase introducida por teclado
print("CONTAR PALABRAS")

cadena=(str(input("Introduzca una frase: ")))

palabras=cadena.split(" ")  

i=0
while(i<len(palabras)): 
    if(palabras[i]==''):
        palabras.remove('')
        i=i-1
    i=i+1

print("Número de palabras: %s"%(len(palabras)))