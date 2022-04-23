import secrets

def merge_sort(lista):

    if len(lista) > 1:

        meio = (len(lista))//2

        lista_esquerda = lista[:meio]
        lista_direita = lista[meio:]

        merge_sort(lista_esquerda)
        merge_sort(lista_direita)

        i,j,k = 0,0,0

        while i<len(lista_esquerda) and j<len(lista_direita):
            if  lista_esquerda[i] < lista_direita[j]:
                lista[k] = lista_esquerda[i]
                i+=1
            else:
                lista[k] = lista_direita[j]
                j+=1
            k+=1

        while i<len(lista_esquerda):
            lista[k]=lista_esquerda[i]
            i+=1
            k+=1

        while j<len(lista_direita):
            lista[k]=lista_direita[j]
            j+=1
            k+=1

    return lista

if __name__=="__main__":
    lista = [secrets.randbelow(1000) for i in range(10)]
    print(lista)
    lista = merge_sort(lista)
    print(lista)
