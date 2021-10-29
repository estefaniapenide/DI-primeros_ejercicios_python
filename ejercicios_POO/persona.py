from dni import Dni

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