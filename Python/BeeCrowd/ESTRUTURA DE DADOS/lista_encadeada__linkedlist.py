class Nodo:

    def __init__(self, item):

        self.item = item
        self.prox = None

class Lista_encad:

    def __init__(self, head = None):
        
        self.head = head
        self.ultimoElem = self.head

    def adicionar(self,valor):

        if self.head == None:
            self.head = Nodo(valor)
        else:
            if self.head.prox == None:
                self.head.prox = Nodo(valor)
                self.ultimoElem = self.head.prox
            else:
                self.ultimoElem.prox = Nodo(valor)
                self.ultimoElem = self.ultimoElem.prox

    def mostrar(self):
        nodo = self.head
        if nodo.item != None:
            print(nodo.item)
            while nodo.prox != None:
                nodo = nodo.prox
                print(nodo.item)

if __name__=="__main__":

    lista = Lista_encad()
    lista.adicionar(1)
    lista.adicionar(2)
    lista.adicionar(3)