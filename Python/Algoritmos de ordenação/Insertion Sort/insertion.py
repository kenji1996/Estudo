import secrets

def insertion_sort(lista):

    size_array = len(lista)
    aux = 0

    for i in range(1, size_array):
        chave = lista[i]
        k = i
        while k > 0 and chave < lista[k-1]:
            lista[k] = lista[k-1]
            k -=1
        lista[k] = chave

if __name__ == "__main__":

    lista = [secrets.randbelow(1000) for i in range(10)]
    print(lista)
    insertion_sort(lista)
    print(lista)