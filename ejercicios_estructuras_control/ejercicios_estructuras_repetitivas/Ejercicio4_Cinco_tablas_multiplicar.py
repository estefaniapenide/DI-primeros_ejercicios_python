#Algoritmo que muestre las tablas de multiplicar de los números 1,2,3,4,5
print("TABLAS DE MULTIPLICAR DEL 1,2,3,4 Y 5")

i=1
num=1
while(num <= 5):
    while(i <= 10):
        sol=i*num
        print("%sx%d=%r"%(i,num,sol))
        i=i+1
    print("\n")
    i=1
    num=num+1