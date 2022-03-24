# A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*106), indicando a quantidade de imóveis
# N linhas contém um par de valores X (1 ≤ X ≤ 10) e Y (1 ≤ Y ≤ 200), indicando a quantidade de moradores de cada imóvel e o respectivo consumo total de cada imóvel (em m3)
# O final da entrada é representado pelo número zero.

#quantidade imoveis
#quantas pessoas vivem (min 1 max 10) / consumo total daquele imovel (1<= X <=200)

ciclo = True
contagem_imovel = 1

class Cidade:

    def __init__(self, qte_imoveis = 1, imoveis = []):
        self.qte_imoveis = qte_imoveis
        self.qte_imoveis = imoveis

class Imovel:

    def __init__(self, pessoas = 1, consumo = 1):
        self.pessoas = pessoas
        self.consumo = consumo

def checar_imovel(imovel):
    if (1<=int(imovel[0])<=10) and (1<=int(imovel)<=200):
        return True
    else:
        return False

while ciclo:

    contagem_imovel = input()
    if int(contagem_imovel) == 0:
        quit()
    cidade = Cidade(int(contagem_imovel))

    for i in range(contagem_imovel,0,-1):
        out = 0
        while not out:
            imovel = input().split()
            out = checar_imovel(imovel)

        imovel = Imovel(int(imovel[0]),int(imovel[1]))
        cidade.imoveis.append(imovel)
    #organiza uma lista
    cidade.imoveis = sorted(cidade.imoveis)
