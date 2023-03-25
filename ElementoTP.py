import random
class ElementoTP:
    def __init__(self, numeroAtomico=None, simbolo=None, elemento=None):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.elemento = elemento
        self.color = "%06x" % random.randint(0, 0xFFFFFF)

    def setNumeroAtomico(self, numeroAtomico):
        self.numeroAtomico = numeroAtomico

    def getNumeroAtomico(self):
        return self.numeroAtomico
    
    def setSimbolo(self, simbolo):
        self.simbolo = simbolo

    def getSimbolo(self):
        return self.simbolo
    
    def setElemento(self, elemento):
        self.elemento = elemento

    def getElemento(self):
        return self.elemento
    
    def getColor(self):
        return self.color