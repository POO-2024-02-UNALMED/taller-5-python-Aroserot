from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    numAnfibios = 0
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Anfibio.listado.append(self)
        Anfibio.numAnfibios += 1

    @classmethod
    def cantidadAnfibios(cls):
        return cls.numAnfibios

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = cls(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra

    def getColorPiel(self):
        return self.colorPiel

    def isVenenoso(self):
        return self.venenoso
