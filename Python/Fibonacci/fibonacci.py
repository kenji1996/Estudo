#   Dado que queremos calcular o digito 50 da sequencia, se guardarmos os valores dos elementos anteriores
#em uma lista, o algoritmo apenas acessa a lista para acessar o valor ao invés de realizer todo o calculo novamente

def fibonacci(n):
    if n<=1:
        return n
    if fibonacci_cache[n] != None:
        return fibonacci_cache[n] 
    numero = (fibonacci(n-1)+fibonacci(n-2))
    fibonacci_cache[n] = numero
    return numero

n = 100
fibonacci_cache = [None] * (n+1)

print(fibonacci(n))