from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    numPeces = 0
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas

        Pez.listado.append(self)
        Pez.numPeces += 1
    
    @classmethod
    def cantidadPeces():
        return Pez.numPeces
    
    def movimiento():
        return "nadar"
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        salmon = Pez(nombre,edad,"oceano",genero,"rojo",6)
        cls.salmones += 1
    
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        bacalao = Pez(nombre,edad,"oceano",genero,"gris",6)
        cls.bacalaos += 1
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getCantidadAletas(self):
        return self.cantidadAletas