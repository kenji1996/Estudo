#pode ser usado para ordenar itens que sao identificados por chaves unicas
#cada chave é uma cadeia de caracteres ou numeros

MAX_CHARS = 28

def radix_sort(lista):

    tamanho_max = max([len(palavra) for palavra in lista])

    