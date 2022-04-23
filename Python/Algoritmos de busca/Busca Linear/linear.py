import secrets

def busca_linear(valor, lista):

    for i in range(len(lista)):
        if lista[i] == valor:
            return i

    return None

if __name__=="__main__":

    lista = [secrets.randbelow(100) for i in range(10)]
    print(lista)
    print(busca_linear(96,lista))