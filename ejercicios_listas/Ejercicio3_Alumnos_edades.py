# Programa que registra nombre y edad de varios alumnos. El proceso
# de lectura de datos termina cuando se introduce como nombre un
# asterisco (*). Al finalizar se muestran:
# - Todos los alumnos mayores de edad
# - Los alumnos mayores (que tienen más edad)
print("ALUMNOS Y SUS EDADES")

nombres=[]
edades=[]

nombre=""
edad=0

while(nombre!="*"):
    nombre=str(input("\nNombre: "))
    if(nombre!="*"):
        nombres.append(nombre)
        edad=int(input("Edad: "))
        edades.append(edad)

print("\nAlumnos mayores de edad:")
i=0
for num in edades:
    if num>=18:
        j=edades.index(num,i)
        print(nombres[j],",",edades[j],"años.")
    i=i+1

print("\nAlumnos más mayores:")
edadmax=max(edades)
i=0
for num in edades:
    if num==edadmax:
        j=edades.index(num,i)
        print(nombres[j],",",edades[j],"años.")
    i=i+1


    
