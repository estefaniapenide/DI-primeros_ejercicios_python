
from persona import Persona
from cuentajoven import CuentaJoven

print("CREACION DE CUENTA JOVEN\n")

print("Introduzca los datos del cliente.")
nombre=(str(input("Nombre:")))
edad=(str(input("Edad:")))
dni=(str(input("DNI:")))

persona=Persona(nombre,edad,dni)



cuentaJoven=CuentaJoven(persona,0,2)

print("\nSe ha creado una cuenta joven.\n")
print(cuentaJoven.mostrar())

ingreso=(int(input("\nCantidad a ingresar(€):")))
cuentaJoven.ingresar(ingreso)
print()
print(cuentaJoven.mostrar())

retirar=(int(input("\nCantidad a retirar(€):")))
cuentaJoven.retirar(retirar)
print()
print(cuentaJoven.mostrar())