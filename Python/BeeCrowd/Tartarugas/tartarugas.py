# 3 tartarugas em 3 posicoes diferentes [x1, y1] [x2, y2] [x3, y3]
# eu posso me movimentar 2 unidades/s (ou 1 diagonal)
# tartarugas podem se movimentar 1 unidade/s

#1th input = x1 y1 da pessoa
#2th-4th = x2 y2 D(direita) ou C(cima) -> para onde a tartaruga vai andar

def calcular_distancia(el1 : list, el2 : list):

    x = abs(int(el1[0])-int(el2[0]))
    y = abs(int(el1[1])-int(el2[1]))

    total_distance = x+y

    return [x,y],total_distance

def coordenadas():
    out = False

    while not out:

        try:
            coordenadas = input()
            coordenadas = coordenadas.split()
            for i in range(0,2,1):
                coordenadas[i] = int(coordenadas[i])
            out = True
        except:
            pass

    return coordenadas

def decidir_rota(el1, el2):

    aux = []

    for i in el2:

        if i[2] == 'D':
            i = direita(i)
        elif i[2] == 'C':
            i = cima(i)

        aux.append(calcular_distancia(el1, i))

    n = 10001
    coord = []
    for i in aux:
        if i[1] < n:
            n = i[1]
            coord = i[0]

    return n,coord

def cima(el):
    return [el[0],el[1]+1]

def direita(el):
    return [el[0]+1,el[1]]

pessoa = coordenadas()

tartarugas = [[2,2,"D"],[3,1,"D"],[4,1,"D"]]

print(direita(tartarugas[0]))

