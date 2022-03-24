#
class Cachorro:
    pass

def checar(c):
    try:
        print('Nome: %d' % c.__name__)
    except:
        print('Nao tem nome mas tem id: %d' % id(c))

#toda funcao, objeto e modulo sao objetos que possuem esses atributos
Dog = Cachorro
d = Cachorro()
c = checar
print(Dog, Dog.__name__)

c(d)