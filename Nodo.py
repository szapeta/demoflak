class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getSiguiente(self):
        return self.siguiente
        