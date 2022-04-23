import secrets

def particionar(array, start, end):
    
    pivo_index = start
    pivo = array[pivo_index]

    while start < end:

        while start < len(array) and array[start] <= pivo:
            start +=1
        

        while array[end] > pivo:
            end -=1

        if (start < end):
            array[start], array[end] = array[end], array[start]

        
    array[end], array[pivo_index] = array[pivo_index], array[end]

    return end

def quicksort(array, start, end):

    if (start < end):

        p = particionar(array, start, end)

        quicksort(array, start, p - 1)
        quicksort(array, p+1, end)

def criar_lista(n):
    lista = [None] * (n)
    for i in range(0, n, 1):
        lista[i] = secrets.randbelow(n)
    return lista

lista = criar_lista(100)
quicksort(lista, 0, len(lista)-1)
print(lista)
