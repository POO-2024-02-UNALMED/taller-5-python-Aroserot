from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    numMamiferos = 0
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitat, genero,pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)
        self.pelaje = pelaje
        self.patas = patas

        Mamifero.listado.append(self)
        Mamifero.numMamiferos += 1

    @classmethod
    def cantidadMamifero():
        return Mamifero.numMamiferos

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        caballo = Mamifero(nombre,edad,"pradera",genero,True,4)
        cls.caballos += 1

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        leon = Mamifero(nombre,edad,"selva",genero,True,4)
        cls.leones += 1
    
    def isPelaje(self):
        return self.pelaje

    def getPatas(self):
        return self.patas