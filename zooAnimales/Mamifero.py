from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    numMamiferos = 0
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas
        Mamifero.listado.append(self)
        Mamifero.numMamiferos += 1

    @classmethod
    def cantidadMamiferos(cls):
        return cls.numMamiferos

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = cls(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = cls(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon

    def isPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas
