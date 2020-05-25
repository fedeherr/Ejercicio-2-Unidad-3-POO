from Helados import Helado
from Sabor import Sabor
from ManejaSabores import manejaSabores
class manejaHelados:
    __listaHelados = []
    __listaIds = []
    def __init__(self, listaHelados = [], listaIds = []):
        self.__listaHelados = listaHelados
        self.__listaIds = listaIds
    def manejarHelado(self, peso, sabores):
        unHelado = Helado(peso, sabores)
        self.__listaHelados.append(unHelado)
    def buscarMaximo(self):
        lista = self.__listaIds
        listamaximos = []
        for i in range(5):
            if (max(lista) != 0):
                indice = lista.index(max(lista))
                lista[indice] = -1
                indice = indice + 100
                listamaximos.append(indice)
        return (listamaximos)
    def inicializarListaIds(self, cantidadsab):
        if (self.__listaIds == []): #Esto verifica si la lista está vacia o no, si esta vacia crear una nueva y si no, devolver todos sus valores a 0
            for i in range(cantidadsab):
                self.__listaIds.append(0)  
        else:
            for i in range(cantidadsab):
                self.__listaIds[i] = 0 
    def saboresVendidos(self, cantidadsab):
        self.inicializarListaIds(cantidadsab)
        for i in range(len(self.__listaHelados)):
            for c in range(self.__listaHelados[i].getNumSabores()):
                ids = self.__listaHelados[i].getidSabores(c) - 100
                self.__listaIds[ids] = self.__listaIds[ids] + 1
        return(self.buscarMaximo())
    def totalGramosVendidos(self, idsabor):
        pesototal = 0
        for i in range(len(self.__listaHelados)):
                for c in range(self.__listaHelados[i].getNumSabores()):
                    if (self.__listaHelados[i].getidSabores(c) == idsabor):
                        pesosabor = self.__listaHelados[i].getPeso() / self.__listaHelados[i].getNumSabores()
                        pesototal = pesototal + pesosabor
        return(pesototal)
    def saboresVendidosGramos(self, gramos, cantidadsab):
        self.inicializarListaIds(cantidadsab)
        listaVendidos = []
        for i in range(len(self.__listaHelados)):
            if (self.__listaHelados[i].getPeso() == gramos):            
                for c in range(self.__listaHelados[i].getNumSabores()):
                    ids = self.__listaHelados[i].getidSabores(c)
                    self.__listaIds[ids-100] = self.__listaIds[ids-100] + 1
        for i in range(len(self.__listaIds)):
            if self.__listaIds[i] != 0: listaVendidos.append(i+100)
        return(listaVendidos)


