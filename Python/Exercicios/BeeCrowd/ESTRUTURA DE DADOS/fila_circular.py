class FilaCircular:

    def __init__(self, tamanho = 5):
        """ Fila circular tem tamanho padrao 5 caso nenhum argumento seja usado """
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.frente = -1
        self.tras = -1

    def inserir(self,valor):

        if self.frente and self.tras == -1:
            self.frente, self.tras = 0,0
            self.fila[self.tras] = valor

        else:
            if self.tras+1 == self.frente:
                print("Fila cheia")
            else:
                self.tras = (self.tras + 1) % self.tamanho
                self.fila[self.tras] = valor

    def remover(self):

        if self.frente == -1:
            print("Sem objetos na lista")

        else:
            aux = self.fila[self.frente]
            self.fila[self.frente] = None
            self.frente = (self.frente + 1) % 5

    def mostrar(self):

        print(self.fila)

if __name__=="__main__":

    filac = FilaCircular()

    filac.inserir(1)
    filac.inserir(1)
    filac.inserir(1)
    filac.inserir(1)



            
