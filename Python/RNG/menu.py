# -*- encoding: utf-8 -*-
import numeros
import os
import time
import sys

sistema_numero = {'00': 'saci', '01': 'seta', '02': 'sino', '03': 'soma', '04': 'serra', '05': 'cela', '06': 'sachê', '07': 'saco', '08': 'sofá', '09': 'sapo', '10': 'taça', '11': 'dado', '12': 'tina(vaso)', '13': 'time', '14': 'terra(planeta)', '15': 'telha/tela', '16': 'tocha', '17': 'taco', '18': 'tufão/TV', '19': 'taboa/diabo', '20': 'nóz', '21': 'índio', '22': 'ninho(pássaro)', '23': 'nome', '24': 'nero', '25': 'nilo', '26': 'anjo', '27': 'nuca', '28': 'nave', '29': 'nabo', '30': 'maçã', '31': 'moto', '32': 'mina(pedra)', '33': 'múmia', '34': 'mar', '35': 'mola', '36': 'miojo', '37': 'maca(médico)', '38': 'máfia', '39': 'mapa', '40': 'rosa', '41': 'rato', '42': 'rena', '43': 'remo', '44': 'arara', '45': 'rolha', '46': 'rocha', '47': 'arca', '48': 'rifa', '49': 'robô', '50': 'laço', '51': 'lata', '52': 'lona', '53': 'lama', '54': 'loro(folha)', '55': 'lula', '56': 'lixa', '57': 'lego', '58': 'lava', '59': 'lupa', '60': 'giz(escola)', '61': 'jato', '62': 'china', '63': 'chama', '64': 'jarro', '65': 'gelo', '66': 'chuchu', '67': 'jaca/shaco', '68': 'chuva', '69': 'chapéu', '70': 'gaze', '71': 'gato', '72': 'cano', '73': 'cama', '74': 'carro', '75': 'galo', '76': 'caixão', '77': 'coco', '78': 'gavião', '79': 'capa', '80': 'vaso', '81': 'foto', '82': 'vinho', '83': 'fumo', '84': 'ferro', '85': 'violão', '86': 'feijão', '87': 'faca', '88': 'favo(mel)', '89': 'fubá', '90': 'poço', '91': 'pato', '92': 'pinha', '93': 'puma(onça)', '94': 'barro', '95': 'pilha', '96': 'peixe', '97': 'boca', '98': 'pavão', '99': 'pipa'}

def contagem_regressiva(tempo):
    time.sleep(tempo)

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def conversao_numero_significado(numero):
    frase = str(numero)
    numeros_separados = ""
    index, n = 0, 2
    frase = [frase[i:i+n] for i in range(0,len(frase),n)]
    for i in frase:
        numeros_separados += i + "  "
        frase[index] = sistema_numero[i]
        index += 1
    return numeros_separados, frase


if __name__=="__main__":

    out = False

    while not out:
        try:
            print("How many numbers?")
            quantidade = int(input())
            print("How much time? (seconds)")
            tempo = int(input())
            settings = numeros.Tentativa(quantidade, tempo)
            limpar_console()
            print(f"{quantidade} digits\n{tempo} seconds to memorize\nType 1 to start")
            digit = int(input())

            if digit == 1:
                limpar_console()
                print(settings.sequencia)
                contagem_regressiva(tempo)
                limpar_console()
                sequence = input("Type in the sequence of numbers\n")
                settings.n_tentativas += 1
                limpar_console()
                print(f"{settings.sequencia}\n{sequence}")
                n_sep, sign = conversao_numero_significado(settings.sequencia)
                print(f"{n_sep}\n{sign}")

        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            print("Invalid input")
            