# Función calcularMaxMin que recibe una lista con valores numéricos y
# devuelve el máximo y el mínimo. El programa pide números por teclado
# y muestra el máximo y el mínimo utilizando la función anaterior.
print("MÁXIMO Y MÍNIMO")

def calcularMaxMin(lista):
    a=max(lista)
    b=min(lista)
    return b,a   

print("\nIntruduzca números. Cuando no quiera introducir más, intruduzca cualquier otro carácter.")

num=1
numeros=[]

a=True
while(a):
    try:
        a=True
        cad=str(input("Número: "))
        num=float(cad)
        numeros.append(num)
    except ValueError:
        a=False

print("\nNúmeros introducidos:",numeros)
if(len(numeros)==0):
    print("No ha introducido ningún número.")
else:
    print("El mínimo y el máximo son respectivamente:",calcularMaxMin(numeros))

        