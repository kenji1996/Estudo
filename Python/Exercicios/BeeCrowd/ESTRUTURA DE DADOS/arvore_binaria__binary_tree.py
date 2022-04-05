#29 03 2022 FUNCIONAL

class Nodo:

    def __init__(self, valor = None):

        self.valor = valor
        self.esquerda = None
        self.direita = None

    def adicionar(self,valor):

        """ Primeiro checa se o nodo possui valor: caso nao tenha, valor do Nodo 1 vira VALOR
        
            Caso self seja um Nodo preenchido, verifica se o VALOR e maior que o valor do nodo.

            Depois da verificação, verifica se os Nodos DIREITA ou ESQUERDA existem.

            Caso NÃO exista, o Nodo é criado com o valor passado como VALOR.

            Caso exista, a função adicionar() é chamada em recursão até chegarmos na folha da árvore.
            
            
            """

        if self.valor == None:
            self.valor = valor
            return


        elif self.valor <= valor:
            if self.direita == None:
                self.direita = Nodo(valor)
                return
            else:
                if self.direita.valor <= valor:
                    self.direita.adicionar(valor)
                return


        elif self.valor > valor:
            if self.esquerda == None:
                self.esquerda = Nodo(valor)
                return
            else:
                if self.esquerda.valor > valor:
                    self.esquerda.adicionar(valor)
                return

    def percorrerSemOrdem(self):    
        print(self.valor, end=' ')
        if self.esquerda:
            self.esquerda.percorrerSemOrdem()
        if self.direita:
            self.direita.percorrerSemOrdem()

    def percorrerEmOrdem(self):
        if self.esquerda:
            self.esquerda.percorrerEmOrdem()
        print(self.valor, end=' ')
        if self.direita:
            self.direita.percorrerEmOrdem()

    def percorrerDepoisOrdem(self):
        if self.esquerda:
            self.esquerda.percorrerDepoisOrdem()
        if self.direita:
            self.direita.percorrerDepoisOrdem()
        print(self.valor, end=' ')

raiz = Nodo(5)
raiz.adicionar(6)
raiz.adicionar(2)
raiz.adicionar(1)


