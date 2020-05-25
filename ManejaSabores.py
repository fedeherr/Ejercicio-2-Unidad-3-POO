from Sabor import Sabor
import csv
class manejaSabores:
    __listaSabores = []
    def __init__ (self, listaSabores = []):
        self.__listaSabores = listaSabores
    def agregarSabor(self, unSabor):
        self.__listaSabores.append(unSabor)
    def __str__(self):
        s = ""       
        for sabor in self.__listaSabores:
            s += str(sabor) + '\n'
        return s
    def saborhelado(self, idsabor = 1):
        if (idsabor != 0):
            for sabor in self.__listaSabores:
                if (sabor.getNum() == idsabor):
                    return sabor
            print ("No se encontró")
            return 0
    def cantidadSab(self):
        return len(self.__listaSabores)
    def manejarSabores(self):
        archivo = open('Sabores.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                "'saltear cabecera'"
                bandera = not bandera
            else:
                    numero = fila[0]
                    nombre = fila[1]
                    descripcion = fila[2]
                    unSabor = Sabor(numero, nombre, descripcion)
                    self.agregarSabor(unSabor)
    def getNombre(self, indice):
        return self.__listaSabores[indice-100].getNomb()
