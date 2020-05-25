class Sabor:
    __numero = 0
    __nombre = 'X'
    __descripcion = 'X'
    def __init__(self, numero = 0, nombre = 'X', descripcion = 'X'):
        self.__numero = numero
        self.__nombre = nombre
        self.__descripcion = descripcion
    def getNum(self):
        return int(self.__numero)
    def getNomb(self):
        return self.__nombre
    def getDesc(self):
        return self.__descripcion
    def __str__(self):
        return "Id %d Helado %s Descripcion %s" % (int(self.__numero), self.__nombre, self.__descripcion)
    