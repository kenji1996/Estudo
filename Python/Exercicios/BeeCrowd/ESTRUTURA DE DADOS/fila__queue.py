class Fila:

    """ Tentativa de fazer Fila """

    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.ultimo_elem = -1
        self.dados = [None] * tamanho

    def vazia(self):
        if self.ultimo_elem == -1:
            return True
        elif self.ultimo_elem >= 0:
            return False

    def cheia(self):
        if self.ultimo_elem == self.tamanho - 1:
            return True
        else:
            return False
    
    def checar_ultimo_elem(self):
        if self.vazia():
            print("Lista vazia")
        else:
            return self.dados[self.ultimo_elem]

    def adicionar(self, informacao):
        if self.cheia():
            print("Lista cheia")
            return
        else:
            self.dados[self.ultimo_elem + 1] = informacao
            self.ultimo_elem += 1

    def remover(self):

        if self.vazia():
            print("Lista vazia")
        else:
            aux = self.dados[0]
            self.dados[0] == None
            if self.vazia():
                self.dados[0] = None
                return aux
            aux_list = [None] * self.tamanho
            j=0
            for i in self.dados:
                if i != None:
                    aux_list[j] = i
                j += 1
            self.dados = aux_list
        return aux

class Queue:

    """ Fila da internet """

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)