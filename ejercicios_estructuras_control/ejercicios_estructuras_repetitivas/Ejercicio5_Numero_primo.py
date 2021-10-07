# Programa que dice si un número introducido por teclado es primo o no
print("NÚMERO PRIMO")

# Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores positivos distintos: él mismo y el 1.
num=int(input("Introduzca un número entero positivo para comprobar si es primo: "))
i=1
div=0
while(i<=num):
    if(num%i==0):
        div=div+1
    i=i+1
if(div==2):
    print("%s es PRIMO"%(num))
else:
    print("%s NO es PRIMO"%(num))