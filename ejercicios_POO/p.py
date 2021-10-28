from dni import Dni

class P:
   
    def __init__(self,nombre="",edad:int=0,dni:Dni=Dni("00000000")):
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
        if( int(edad)>=0):
            self.__edad=edad
        else:
            self.__edad=0
            print("EDAD INCORRECTA")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,dni):
        self.__dni=dni
    
    def mostrar(self):
        return self.__nombre+" ("+str(self.edad)+")"

    def esMayorDeEdad(self):
        esMayor=False
        if(int(self.edad)>=18):
            esMayor=True
        return esMayor

