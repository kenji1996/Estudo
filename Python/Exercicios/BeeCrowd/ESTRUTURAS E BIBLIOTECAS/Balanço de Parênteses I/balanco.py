expressoes = ""
qte_linhas = 0
sinal = 0
out = False

while True:
    expressoes = input()
    if len(expressoes) == 0:
        print("incorrect")
    elif len(expressoes) > 10000:
        expressoes = ""
    if len(expressoes) != 0:

        for i in expressoes:
            if i == ")" and sinal == 0:
                sinal -= 1
                break
            elif i == "(":
                sinal += 1
            elif i == ")":
                sinal -= 1
        if sinal == 0:
            print("correct")
        else:
            print("incorrect")

    sinal = 0

