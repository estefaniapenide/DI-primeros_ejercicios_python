
class Dni:
    def __init__(self,numero):
        self.numero=numero
    
    def __calcular_letra(self):
        letras='TRWAGMYFPDXBNJZSQVHLCKE'  
        return letras[int(self.numero)%23]

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,numero):
        if len(numero)==8 and numero.isdigit():
            self.__numero=numero
            self.__letra=self.__calcular_letra()
        else:
            self._numero=0
            self.__letra=""
            print("DNI Incorrecto")
            
    @property
    def letra(self):
        return self.__letra

    def mostrar(self):
        return self.numero+self.letra

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
        if (len(dni)==9):
            numero=""
            i=0
            while(i<8):
                numero=numero+dni[i]
                i+=1               
            letra=dni[8]
            dniCorrecto=Dni(numero)
            if(dniCorrecto.letra==letra):
                self.__dni=dni
        else:
            self.__dni="*FALTA DNI*"
            print("DNI INCORRECTO")
    
    def mostrar(self):
        return self.nombre+" ("+str(self.edad)+") "+self.dni

    def esMayorDeEdad(self):
        esMayor=False
        if(self.__edad.isdigit() and int(self.edad)>=18):
            esMayor=True
        return esMayor

class Cuenta:

    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad

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
        if(importe>0):
            self.__cantidad=self.__cantidad-importe
            print("Importe retirado: "+str(importe)+"€")
        else:
            self.__cantidad=self.__cantidad
            print("No es posible retirar "+str(importe)+"€")

    def ingresar(self,importe):
        if(importe<0):
            self.__cantidad=self.__cantidad
            print("No es posible ingresar "+str(importe)+"€")
        else:
            self.__cantidad=self.__cantidad+importe
            print("Importe ingresado: "+str(importe)+"€")
    
    def mostrar(self):
        return self.__titular.mostrar()+" "+str(self.__cantidad)+"€"

class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
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
            print("No es un titular válido. No puede retirar dinero de esta cuenta.")
       

    def ingresar(self,importe):
        super().ingresar(importe)
    
    def mostrar(self):
        return "Cuenta joven"+"\nTitular: "+super().titular.mostrar()+"\nBonificacion:"+str(self.__bonificacion)+"%"+"\nCantidad:"+str((super().cantidad))+"€"



