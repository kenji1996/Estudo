import secrets

def create_random_list(n = 10, intervalo = 100):

    lista = [None] * n

    for i in range(len(lista)):
        lista[i] = secrets.randbelow(intervalo)

    return lista

#FUNCIONANDO 22 04 2022

def selection(array : list):

    size_array = len(array)
    aux = 0

    # iterar pelo array comecando por 0
    for i in range(size_array):
        #variavel auxiliar q guarda o indice do menor valor, tendo como valor inicial o inicio do for loop
        aux = i
        for j in range(i,size_array):
            if array[j] <= array[aux] :
                aux = j
        array[i], array[aux] = array[aux], array[i]

if __name__=="__main__":

    lista = create_random_list(10,10000)
    print(lista)
    selection(lista)
    print(lista)