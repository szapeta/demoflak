from Nodo import Nodo
import graphviz

class ListaSimpleTP:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def agregar(self, elemento):
        nodoTmp = Nodo(elemento)
        if(not self.blnExisteNumeroAtomico(elemento)):
            if self.primero == None:
                self.primero = nodoTmp
                self.ultimo = nodoTmp
            else:
                self.ultimo.setSiguiente(nodoTmp)
                self.ultimo = nodoTmp
            self.size += 1
        else:
            print("El elemento ya existe")

    def blnExisteNumeroAtomico(self, elementoQuimicoNuevo):
        if(self.size > 0):
            nodoTemp = self.primero
            while(nodoTemp != None):
                if(nodoTemp.getValor().getNumeroAtomico() == elementoQuimicoNuevo.getNumeroAtomico()):
                    return True
                nodoTemp = nodoTemp.getSiguiente()
        return False

    def printNodos(self):
        nodoTemp = self.primero
        while(nodoTemp != None):
            print(nodoTemp.getValor().getNumeroAtomico(), nodoTemp.getValor().getSimbolo(), nodoTemp.getValor().getElemento(), nodoTemp.getValor().getColor())
            nodoTemp = nodoTemp.getSiguiente()

    def generarDot(self):
        nodoTemp = self.primero
        dot = graphviz.Digraph('structs', filename='structs.gv', node_attr={'shape': 'none', 'fontname':'Helvetica'})
        
        strTabla = "<table>"

        while(nodoTemp != None):
            strTabla += f'<tr><td bgcolor="#{nodoTemp.getValor().getColor()}" width="60" height="60" border="0">{nodoTemp.getValor().getNumeroAtomico()}{nodoTemp.getValor().getSimbolo()} {nodoTemp.getValor().getElemento()}</td></tr>'
            nodoTemp = nodoTemp.getSiguiente()
        
        strTabla += "</table>"

        dot.node('n', label='<' +strTabla+'>')
        dot.render(outfile='img/structs.svg').replace('\\', '/')
        'img/structs.svg'