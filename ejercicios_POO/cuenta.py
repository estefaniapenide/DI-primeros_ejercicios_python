from persona import Persona

class Cuenta:

    def __init__(self,titular:Persona,cantidad=0):
        self.titular=titular
        self.cantidad=cantidad

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular=titular

    @property
    def cantidad(self):
        return self.__cantidad

    def retirar(self,importe):
        self.__cantidad=self.__cantidad-importe

    def ingresar(self,importe):
        if(importe<0):
            self.__cantidad=self.__cantidad
        else:
            self.__cantidad=self.__cantidad+importe
    
    def mostrar(self):
        return self.__titular+" "+str(self.__cantidad)+"€"
 
