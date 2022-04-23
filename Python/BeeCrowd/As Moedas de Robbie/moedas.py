""" A primeira linha de um caso de teste contém um inteiro M (2 ≤ M ≤ 20 ) que representa a quantidade de moedas """
""" Cada uma das próximas M linhas contém um inteiro Vi (1 ≤ Vi ≤ 500) que representa o valor da moeda Mi """
""" por último um inteiro N (1 ≤ N ≤ M) que é o salto na soma escolhido por Glória. """

""" Imprima “You’re a coastal aircraft, Robbie, a large silver aircraft.”, caso Glória ganhe o jogo (sair numero primo) """
""" Bad boy! I’ll hit you.”, caso Glória não ganhe o jogo (nao sair numero primo). A saída não deve conter aspas. """

# 17/03/2022 working

def n_moedas():
    
    n_moedas = 0
    out = False
    while not out:
        try:
            print("Numero de moedas?")
            n_moedas = input()
            n_moedas = int(n_moedas)
            out = True
        except:
            pass

    return n_moedas

def valor_moedas(n_moedas : int):
    out = False
    while not out:
        valor_moedas = []
        for i in range(0,n_moedas,1):
            try:
                valor = input()
                valor = int(valor)
                valor_moedas.append(valor)
            except:
                print("invalido carallho")
                break
            if len(valor_moedas) == n_moedas:
                out = True
    
    return valor_moedas

def n_primo(valor_moedas : list, intervalo : int):

    soma_moedas = 0
    primo = True

    for i in range(0, len(valor_moedas), intervalo):
        soma_moedas += valor_moedas[i]

    for i in range(soma_moedas-1, 1, -1):
        if soma_moedas % i == 0:
            primo = False
        
    return primo

if __name__ == "__main__":

    primo = False

    while not primo:

        n_moedas_int = 0
        valor_moedas_int = []

        n_moedas_int = n_moedas()
        valor_moedas_int = valor_moedas(n_moedas_int)

        out = False
        intervalo = 0

        while not out:
            try:
                intervalo = input()
                intervalo = int(intervalo)
                out = True
            except:
                print("Invalid input")

        primo = n_primo(valor_moedas_int, intervalo)

        if not primo:
            print("Bad boy! I’ll hit you.")
        else:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
