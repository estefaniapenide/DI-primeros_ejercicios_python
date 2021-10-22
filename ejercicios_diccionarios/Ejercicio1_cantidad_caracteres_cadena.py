# Lee una cadena y devuelve un diccionario con la cantidad
# de apariciones de cada caracter en la cadena
print("CARACTERES EN LA CADENA")

lista=[]
diccionario={}

cadena=str(input("\nIntroduce una cadena: "))
cadena=cadena.lower()

contador=0

for a in cadena:
    if a not in diccionario:
        diccionario[a]=1
    else:
        contador=diccionario[a]
        contador=contador+1
        diccionario[a]=contador

print("Cantidad de veces que aparece cada caracter: ")
print(diccionario)