# Lee por teclado las 5 notas obtenidas por un alumno (comprendidas
# entre 0 y 10). A continuación, debe mostrar: todas las notas,
# la nota más alta que ha sacado y la menor
print("NOTAS DEL ALUMNO")

print("\nIntroduzca las notas del alumno una a una")

notas=[]

i=0
while(i<5):
    nota = float(input("Nota: "))
    if(nota<0 or nota>10):
        print("Nota no válida. Las notas deben estar comprendidas entre 0 y 10.")
    else:
        notas.append(nota)
        i=i+1


notamedia=sum(notas)/len(notas)
notaAlta=max(notas)
notaBaja=min(notas)

print("\nNotas: ",notas)
print("Nota media: ",notamedia)
print("Nota más alta: ",notaAlta)
print("Nota más baja: ",notaBaja)