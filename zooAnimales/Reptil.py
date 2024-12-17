from zooAnimales.animal import Animal

class Reptil(Animal):
    listado = []
    numReptiles = 0
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Reptil.listado.append(self)
        Reptil.numReptiles += 1

    @classmethod
    def cantidadReptiles(cls):
        return cls.numReptiles

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = cls(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = cls(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1
        return serpiente

    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola