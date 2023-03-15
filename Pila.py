from Nodo import Nodo

class Pila:
    def __init__(self):
        self.tope = None
        self.valor = None

    def insertar(self, valor):

        if self.tope == None:
            self.tope = Nodo(valor)
        else:
            nodoTemp = Nodo(valor)
            nodoTemp.setSiguiente(self.tope)
            self.tope = nodoTemp

    def printPila(self):
        nodoTemp = self.tope
        listaDatos = ""
        while nodoTemp != None:
            listaDatos += nodoTemp.getValor()
            nodoTemp = nodoTemp.getSiguiente()
        return listaDatos