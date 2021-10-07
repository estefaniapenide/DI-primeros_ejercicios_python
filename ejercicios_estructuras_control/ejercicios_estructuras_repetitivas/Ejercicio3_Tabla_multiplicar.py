# Algoritmo que muestre la tabla de multiplicar de un número introducido por teclado
print("TABLA DE MULTIPLICAR")

# Lo defino como float para poder hacer tablas de multiplicar de números decimales y tampoco restrinjo las tablas sólo a números positivos
num=float(input("Introduzca el número del que quiere obtener su tabla de multiplicar: "))

i=1

while(i <= 10):
    sol=i*num
    print("%sx%d=%r"%(i,num,sol))
    i=i+1