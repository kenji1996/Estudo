#1 linha = n de linhas
#resto = todos os valores

#VERY slow algorithm
def primo(n):
    aux = n-1
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    while aux >= 2:
        valor = n % aux
        if valor == 0:
            return False
        aux -= 1
    return True

#WAY faster algorithm
def primo2(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return 0

linhas = input()
linhas = int(linhas)

for i in range(0,linhas,1):
    n_primo = input()
    n_primo = primo(int(n_primo))
    print(n_primo)
    