from dni import Dni

class Persona:

    

    def __init__(self,nombre="",edad="",dni=""):
        self.nombre=nombre
        self.edad=edad
        self.__dni=dni
    
    def __calcular_letra(self,numero):
        letras='TRWAGMYFPDXBNJZSQVHLCKE'  
        return letras[int(numero)%23] 

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
        if(edad.isdigit()):
            self.__edad=edad
        else:
            print("LA EDAD DEBE SER UN ENTERO")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def nombre(self,dni):
        if (len(dni)==9):
            numero=""
            i=0
            while(i<7):
                numero=numero+dni[i]
                i+=1
            letra=numero[8]
            if (numero.isdigit()):
                if(self.__calcular_letra(numero)==letra):
                    self.__dni=dni
                else:
                    self.__dni=""
                    print("LETRA DE DNI INCORRECTA")
            else:
                self.__dni=""
                print("DNI INCORRECTO") 
        else:
            self.__dni=""
            print("DNI INCORRECTO")