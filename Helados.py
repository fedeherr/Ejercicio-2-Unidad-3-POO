from Sabor import Sabor
class Helado:
    __gramos = 0
    def __init__(self, gramos = 0, sabores = []):
        self.__sabores = sabores
        self.__gramos = gramos
    def mostrarHelado(self):
        print ("Peso total: " + str(self.__gramos))
        print ("Sabores: ")
        for i in range(len(self.__sabores)-1):
            print (self.__sabores[i].getNomb())
    def getPeso(self):
        return int(self.__gramos)
    def getNumSabores(self):
        return len(self.__sabores)-1
    def getidSabores(self, ids):
        return self.__sabores[ids].getNum() 


