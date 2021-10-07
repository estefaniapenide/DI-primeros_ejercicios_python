# Algoritmo que pide números hasta que se introduzca un cero.
# Debe imprimir la suma y la media de todos los números introducidos

print("SUMA Y MEDIA DE NÚMEROS")

print('''Para calcular la suma y la media de varios números, váyalos introduciendo según se van pidiendo.
Cuando no quiera introducir más, pulse 0.\n''')
num=""
suma=0
contador=1
while(num!=0):
    num=float(input("Introzuca un número: "))
    suma=suma+num
    contador=contador+1
media=suma/(contador-2)
print("\nSuma: %s"%(suma))
print("Media: %.2f"%(media))