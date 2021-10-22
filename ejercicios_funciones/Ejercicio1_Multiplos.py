# Pide dos números eneteros al ususario y dice si alguno de ellos
# es múltiplo del otro. L afunción esMultiplo recibe los dos números
# y devuelve si el primero es múltiplo del segundo
print("MÚLTIPLOS\n")

def esMultiplo(a,b):
    if(a%b==0):
        print(a,"es múltiplo de",b)
    else:
        print(a,"NO es múltiplo de",b)

error="ERROR. Debe introducir un número entero."

while(True):
    try:
        num1=int(input("Introduzca un número entero: "))
        break
    except ValueError:
            print(error)

while(True):
    try:
        num2=int(input("Introduzca otro número entero: "))
        break
    except ValueError:
            print(error)
            
print("\nSolución:")
esMultiplo(num1,num2)