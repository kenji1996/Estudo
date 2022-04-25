import time

class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.ant = self
        self.prox = self

class Deque:

    def __init__(self, cabeca = None):
        self.cabeca = cabeca
        self.ultimo = cabeca

    def tamanho(self):
        if self.cabeca == None:
            print("Deque vazio")
        else:
            #CONTINUAR AQUI
            pass

    def adicionar(self, valor):
        nodo = Nodo(valor)
        if self.cabeca.ant == self.cabeca:
            self.cabeca.ant = nodo
            self.cabeca.prox = None
            self.ultimo = nodo
        else:
            self.ultimo.ant = nodo
            self.ultimo.prox = self.ultimo
            self.ultimo = nodo
            nodo.ant = self.cabeca

    def mostrar(self):

        aux = self.cabeca.ant
        if aux == self.cabeca:
            print(self.cabeca.valor)
            return

        while aux != self.cabeca:
            print(aux.valor)
            aux = aux.ant

    def remover(self,valor):
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.ant
        aux = self.cabeca.ant
        while aux != self.cabeca:
            if aux.valor == valor:
                aux.ant.prox = aux.prox
                aux.ant.ant = aux.ant
                return True
            print(aux.valor)
            aux = aux.ant
        return False

deque = Deque(Nodo(10))
for i in range(0,10):
    deque.adicionar(i)
            