

class Persona:
    def __init__(self,nombre="",edad="",dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        if(edad.isdigit() and int(edad)>=0):
            self.__edad=edad
        else:
            self.__edad="*"
            print("LA EDAD DEBE SER UN NÚMERO ENTERO POSITIVO")
    
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,dni):
        self.__dni=dni

    def mostrar(self):
        print("Nombre:"+self.__nombre+"\nEdad:"+self.__edad+"\nDNI:"+self.__dni)
    
    def esMayorDeEdad(self):
        mayorDeEdad=False
        if(self.__edad>=18):
            mayorDeEdad=True
        return mayorDeEdad



class Cuenta:

    def __init__(self,titular,cantidad=""):
        self.titular=titular
        self.catidad=cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        self.__titular=titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    def ingresar(self,importe):
        if(importe>=0):
            self.__cantidad=self.__cantidad+importe
            print("Ingreso realizado.")
        else:
            self.__cantidad=self.__cantidad
            print("No es posible realizar el ingreso.")
    
    def retirar(self,importe):
        if(importe>=0):
            self.__cantidad=self.__cantidad-importe
            print("Retirada realizado.")
        else:
            self.__cantidad=self.__cantidad
            print("No es posible realizar la retirada.")


    def mostrar(self):
        print("Titular:"+str(self.__titular.mostrar())+"\nCantidad(€):"+str(self.__cantidad))




persona=Persona("Juan","2","53191630J")
cuenta=Cuenta(persona)
cuenta.ingresar(20)
cuenta.mostrar()

