# Algoritmo que:
# - Crea una tabla (lista con dos dimensiones) de 5x5 enteros
# - Carga la tabla con valores numéricos enteros
# - Suma los elementos de cada fila y todos los elementos de cada
#   columna visualizando los resultados por pantalla
print("TABLA DE ENTEROS 5X5")
# No se puede crear una tabla de 5x5 vacía. Una tabla vacía por defición tendrá
# dimensiones 0x0. Si tiene una dimensión determinada distinta de cero, 
# tiene que tener elementos dentro. Por ello, el algortimo creará la tabla vacía 
# y luego añadirá los valores enteros hasta alcanzar las dimensiones 5X5. 
# (Podría interpreatrase que el primer paso pide una tabla 5x5 llena de ceros,
#  pero no se trataría de una tabla vacía).

print("\nCreación de tabla vacía:")
tabla=[]
print(tabla)

print("\nCreación de tabla 5x5 con valores enteros:")

import random

for j in range(0,5):
    fila = []
    for i in range(0,5):
        n = random.randint(0,50)
        fila.append(n)
    tabla.append(fila)

print(tabla)

print("\nSuma elementos de cada fila")
j=0
for fila in tabla:
    print("Fila",j+1,":",sum(fila))    
    j=j+1

print("\nSuma elementos de cada columna")
j=0
while(j<len(tabla)):
    i=0
    sumaColumna=0
    while (i<len(tabla)):
        sumaColumna=sumaColumna+tabla[i][j]
        i=i+1
    print("Columna",j+1,":",sumaColumna)
    j=j+1


