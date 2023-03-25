from ListaSimpleTP import ListaSimpleTP
from ElementoTP import ElementoTP
import xml.etree.ElementTree as ET


tree = ET.parse('entrada_proyecto2_dummy.xml')
data = tree.getroot()

miLista = ListaSimpleTP()

for item in data:
    if(item.tag == "listaElementos"):
        for lista in item.iter("listaElementos"):
            for eq in lista.iter("elemento"):
                miLista.agregar(ElementoTP(int(eq.find("numeroAtomico").text), eq.find("simbolo").text, eq.find("nombreElemento").text))

miLista.printNodos()
miLista.generarDot()