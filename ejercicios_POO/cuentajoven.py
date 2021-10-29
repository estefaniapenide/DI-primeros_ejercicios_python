from cuenta import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        if (super().titular.esMayorDeEdad()):
            self.__cuentaValida=True
            print("Titular válido")
        else:
            self.__cuentaValida=False
            print("No es un titular válido")
            
        self.bonificacion=bonificacion

    @property
    def cuentaValida(self):
        return self.__cuentaValida
    
    
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def esTitularValido(self):
        titularValido=False
        if super().titular.esMayorDeEdad() and int((super().titular.edad))<25:
            titularValido=True
        return titularValido

    def retirar(self,importe):
        if(self.esTitularValido()):
            super().retirar(importe)
        else:
            print("Este titular NO puede retirar dinero de esta cuenta.")
       

    def ingresar(self,importe):
        super().ingresar(importe)
    
    def mostrar(self):
        return "Cuenta joven"+"\nTitular: "+super().titular.mostrar()+"\nBonificacion:"+str(self.__bonificacion)+"%"+"\nCantidad:"+str((super().cantidad))+"€"