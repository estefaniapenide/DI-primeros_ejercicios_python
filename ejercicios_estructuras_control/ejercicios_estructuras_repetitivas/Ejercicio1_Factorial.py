# Se pide un número y se calcula su factorial

print("CÁLCULO DE FACTORIAL")

num=int(input("Introduzca un número entero para calcular su factorial: "))

if(num>=0):
    contador=1
    factorial=1
    while(num >= contador):
        factorial=factorial*contador
        contador=contador+1
        print(factorial)

    print("%d!=%s" % (num,factorial))
else:
    print("El cálculo del factorial de un número solo se aplica a números enteros positivos y el cero.")