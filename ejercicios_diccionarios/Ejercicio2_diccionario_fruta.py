# Diccionario para guardar precios de distintas frutas
# Se pide el nombre de la fruta y la cantidad que se ha vendido
# y se muestra el precio final de la fruta a partir de los datos
# guardados en el diccionario. Si la fruta no existe nos dará
# un error. Tras cada consulta el programa nos pregunta
# si queremos hacer otra consulta
print("PRECIO DE LA FRUTA\n")

# diccionario con frutas y precios por Kg
diccionario={'naranja':1.5,'limón':1.9,'fresa':4.8,'kiwi':3.7,'pera':1.7}

precio=0
precioTotal=0
cantidad=0
pregunta="s"

while pregunta=="s":
    while True:
        try:
            fruta=str(input("Fruta: "))
            fruta=fruta.lower()
            precio=diccionario[fruta]
            break
        except KeyError:
            print("ERROR. La fruta no se encuentra en la lista.")

    while True:
        try:
            cantidad=float(input("Cantidad(kg): "))
            break
        except ValueError:
            print("ERROR. Debe introducir un número.")

    precioTotal=precio*cantidad
    print(cantidad,"kg de",fruta,"son",round(precioTotal,2),"€.")

    pregunta=str(input("\n¿Desea hacer otra consulta?(s/n)"))

    pregunta=pregunta.lower()

      

