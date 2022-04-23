""" Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.
Saída
Para cada entrada, deve-se apresentar a mensagem criptografada.
Exemplo de Entrada / Exemplo de Saída
4

Texto #3
abcABC1
vxpdylY .ph
vv.xwfxo.fd

3# rvzgV
1FECedc
ks. \n{frzx
gi.r{hyz-xx

"""

# 1 input = qte de linhas
# 2+ input = conteudo

# primeiro, caracter minusculo e maiusculo
# fica +3 em int (a vira d, A = D)

#segundo, inverte os caracteres
# “3# rw{hW” = “Wh{wr #3”

#terceiro, metade+ da string fica -1
# 3# rw{hW = 3# rvzgV

#ascii A-Z 65-90
#ascii a-z 97-122

class Mensagem:

    def __init__(self, numero_linhas = 0, texto=[]):
        self.numero_linhas = numero_linhas
        self.texto = texto

def substituir_alfabeto(string : str):
    nova_string = ""
    for i in string:
        numero_i = ord(i) # valor UniCode de i
        char_i = chr(numero_i) # chr() method returns a character (a string) from an integer (represents unicode code point of the character).
        #ascii A-Z 65-90
        #ascii a-z 97-122
        if ((numero_i >= 65) and (numero_i <= 90)) or ((numero_i >= 97) and (numero_i <= 122)):
            char_i = chr(numero_i+3)
        nova_string += char_i
    return nova_string

def inverter(string : str):
    n_char = len(string) - 1
    nova_string = ""

    while(n_char >= 0):
        nova_string += string[n_char]
        n_char -= 1
    return nova_string

def substituir_metade(string : str):
    n_char = int(len(string) / 2 + len(string) % 2)
    half = int(len(string) / 2)
    nova_string = string[:half]

    while(n_char != len(string)):
        i = string[n_char]
        numero_i = ord(i)
        char_i = chr(numero_i-1)
        nova_string += char_i
        n_char += 1

    return nova_string

def aplicar_criptografia(string : str):

    aux_string = ""
    aux_string = substituir_alfabeto(string)
    aux_string = inverter(aux_string )
    aux_string = substituir_metade(aux_string)

    return aux_string

passar = False
texto = ""
mensagem = Mensagem()

while not passar:
    try:
        while (mensagem.numero_linhas < 1) or (mensagem.numero_linhas > 1*(10^4)): 
            mensagem.numero_linhas = int(input("Number of lines?"))
        qte_linhas = mensagem.numero_linhas
        while(qte_linhas > 0):
            while (len(texto) < 1) or (len(texto) > 1*(10^3)):
                texto = input()
            mensagem.texto.append(texto)
            qte_linhas -= 1
            texto = ""
        passar = True
    except:
        print("Integers only")

for i in mensagem.texto:
    print(aplicar_criptografia(i))

    

