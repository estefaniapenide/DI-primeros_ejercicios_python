# Programa que inicializa una lista con 10 valores aleatorios
# (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la 
#lista junto con su cuadrado y su cubo
print("NUMEROS CON SU CUADRADO Y SU CUBO")

import random
lista = []
for i in range(0,10):
    n = random.randint(1,10)
    lista.append(n)

print("\nNúmero  Cuadrado  Cubo")

for a,b,c in zip(lista,lista,lista):
    print(a,"      ",b**2,"       ",c**3)




