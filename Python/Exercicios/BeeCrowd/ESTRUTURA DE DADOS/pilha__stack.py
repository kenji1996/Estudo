class Pilha():
    """ Tem uma lista de tamanho especifico preenchido inicialmente com None """

    def __init__(self, tamanho = 5):
        self.tamanho = tamanho
        self.dados = [None] * tamanho
        self.topo = -1

    def adicionar(self,informacao):
        if self.topo == self.tamanho-1:
            print("Pilha cheia")
        else:
            self.dados[self.topo+1] = informacao
            self.topo += 1

    def remover(self):
        if self.topo == -1:
            print("Pilha vazia")
            return
        else:
            aux = self.dados[self.topo]
            self.dados[self.topo] = None
            self.topo -= 1
        return aux

if __name__=="__main__":

    stack = Pilha(tamanho=5)
    for i in range(0,10,1):
        stack.adicionar(i)
    
    print(stack.dados)

    print(stack.remover())

    print(stack.dados)

    print(stack.remover())

    print(stack.dados)

    print(stack.remover())

    print(stack.dados)

    print(stack.remover())

    print(stack.dados)

    print(stack.remover())

    print(stack.dados)

    print(stack.remover())

    print(stack.dados)


