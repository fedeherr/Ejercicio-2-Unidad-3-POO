from ManejaSabores import manejaSabores
from ManejaHelados import manejaHelados
class Menu:
    __switcher=None
    __manejosabor = manejaSabores()
    __manejohelado = manejaHelados()
    def __init__(self):
        self.__manejosabor.manejarSabores()
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        print ("Lista de helados:")
        print (self.__manejosabor)
        idsabor = 1
        peso = 1
        bandera = False
        sabores = []
        sabor = None
        while (idsabor != 0):
            idsabor = int(input("Ingrese el codigo del sabor a agregar, si termino de agregar ingrese 0: "))
            sabor = self.__manejosabor.saborhelado(idsabor)
            if (sabor in sabores): print ("Este sabor ya está en el pedido")
            if ((sabor != 0) & (sabor not in sabores)): sabores.append(sabor)
        while (not bandera):
            print("Ingrese el peso del helado (solo valor númerico)")
            peso = int(input("Pesos disponibles: 100gr, 150gr, 250gr, 500gr, 1000gr: "))
            if ((peso == 100) or (peso == 150) or (peso == 250) or (peso == 500) or (peso == 1000)): bandera = True
            else: print("Ingreso un peso incorrecto")
        self.__manejohelado.manejarHelado(peso, sabores)
    def opcion2(self):
        a = self.__manejosabor.cantidadSab() + 1
        masvendidos = self.__manejohelado.saboresVendidos(a)
        print ("Los 5 helados más vendidos son: ")
        for i in range(len(masvendidos)):
            print (self.__manejosabor.getNombre(masvendidos[i]))
    def opcion3(self):
        a = int(input("Ingrese el sabor a buscar: "))
        print ("De este sabor se vendieron: " + str(self.__manejohelado.totalGramosVendidos(a)) + " gramos")
    def opcion4(self):
        a = int(input("Ingrese el peso a buscar "))
        b = self.__manejosabor.cantidadSab() + 1
        saboresvendidos = self.__manejohelado.saboresVendidosGramos(a, b)
        print ("De este peso se vendieron los siguientes sabores: ")
        for i in range(len(saboresvendidos)):
            print (self.__manejosabor.getNombre(saboresvendidos[i]))