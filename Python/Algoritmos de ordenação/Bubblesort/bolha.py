import secrets

#FUNCIONANDO 22 04 2022

def bubblesort(lista):
    size_array = len(lista)
    pronto = False

    while not pronto:
        pronto = True
        for i in range(1,size_array):
            if lista[i] < lista[i-1]:
                lista[i],lista[i-1] = lista[i-1],lista[i]
                pronto = False

if __name__=="__main__":

    lista = [secrets.randbelow(100) for i in range(10)]
    print(lista)
    bubblesort(lista)
    print(lista)