# -*- encoding: utf-8 -*-
from re import UNICODE
import secrets
from tarfile import ENCODING
from numpy import unicode_
import pandas as pd

sistema_numero = {'0': 'saci', '1': 'seta', '2': 'sino', '3': 'soma', '4': 'serra', '5': 'cela', '6': 'sachê', '7': 'saco', '8': 'sofá', '9': 'sapo', '10': 'taça', '11': 'dado', '12': 'tina(vaso)', '13': 'time', '14': 'terra(planeta)', '15': 'telha/tela', '16': 'tocha', '17': 'taco', '18': 'tufão/TV', '19': 'taboa/diabo', '20': 'nóz', '21': 'índio', '22': 'ninho(pássaro)', '23': 'nome', '24': 'nero', '25': 'nilo', '26': 'anjo', '27': 'nuca', '28': 'nave', '29': 'nabo', '30': 'maçã', '31': 'moto', '32': 'mina(pedra)', '33': 'múmia', '34': 'mar', '35': 'mola', '36': 'miojo', '37': 'maca(médico)', '38': 'máfia', '39': 'mapa', '40': 'rosa', '41': 'rato', '42': 'rena', '43': 'remo', '44': 'arara', '45': 'rolha', '46': 'rocha', '47': 'arca', '48': 'rifa', '49': 'robô', '50': 'laço', '51': 'lata', '52': 'lona', '53': 'lama', '54': 'loro(folha)', '55': 'lula', '56': 'lixa', '57': 'lego', '58': 'lava', '59': 'lupa', '60': 'giz(escola)', '61': 'jato', '62': 'china', '63': 'chama', '64': 'jarro', '65': 'gelo', '66': 'chuchu', '67': 'jaca/shaco', '68': 'chuva', '69': 'chapéu', '70': 'gaze', '71': 'gato', '72': 'cano', '73': 'cama', '74': 'carro', '75': 'galo', '76': 'caixão', '77': 'coco', '78': 'gavião', '79': 'capa', '80': 'vaso', '81': 'foto', '82': 'vinho', '83': 'fumo', '84': 'ferro', '85': 'violão', '86': 'feijão', '87': 'faca', '88': 'favo(mel)', '89': 'fubá', '90': 'poço', '91': 'pato', '92': 'pinha', '93': 'puma(onça)', '94': 'barro', '95': 'pilha', '96': 'peixe', '97': 'boca', '98': 'pavão', '99': 'pipa'}

class Tentativa:

    def __init__(self, quantidade=20, tempo=60):

        self.quantidade = quantidade
        self.tempo = tempo
        self.sequencia = ''.join([str(secrets.randbelow(10)) for i in range(0,self.quantidade)])
        self.n_tentativas = 0
        self.seq_tentativas = []

    def set_quantidade(self,quantidade):
        self.quantidade = quantidade

    def set_sequencia(self):
        self.sequencia = ''.join([str(secrets.randbelow(10)) for i in range(0,self.quantidade)])

    def set_tempo(self,tempo):
        self.tempo = tempo

def converter_txt_csv(dir, separator):
    read_file = pd.read_csv (dir,sep=separator)
    read_file.to_csv (dir)
        
if __name__=="__main__":
    #Convertendo arquivo txt para csv

    print(sistema_numero)