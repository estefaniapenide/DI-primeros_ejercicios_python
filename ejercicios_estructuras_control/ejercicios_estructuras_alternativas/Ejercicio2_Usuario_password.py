# Se pide un nombre de usuario y una contraseña. 
# Si se introduce "pepe" y "asdasd" se indica "Has entrado en el sistema",
# si no se da un error.

print("USUARIO Y CONTRASEÑA")

nom="pepe"
cont="asdasd"

usuario=input("Introduzca su nombre de usuario: ")
password=input("Introduzca su nombre de contraseña: ")

if(usuario==nom and password==cont):
    print("Has entrado en el sistema")
else:
    print("Error. Usuario o contraseña incorrectos")