#1 qte de linhas
#2 <..><.<..>>

#verificar quantos <> (diamantes) existem

import re

qte_linhas,menor,maior = 0,0,0
texto = ""

while True:
    try:
        qte_linhas = int(input())
        break
    except:
        pass

for i in range(0,qte_linhas, 1):
    while (len(texto) == 0 or len(texto) > 1000) or not any((c in set("<.>")) for c in texto):
        texto = input()
    for i in texto:
        if i == "<":
            menor += 1
        elif i == ">":
            maior += 1
    if maior > menor:
        print(menor)
    elif menor >= maior:
        print(maior)
    maior,menor = 0,0
    texto = ""
