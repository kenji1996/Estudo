numeros = [1,1]

while ((numeros[0] != 0) and (numeros[1] != 0)):
    numeros = input()
    numeros = [int(i) for i in numeros.split()]
    if (1 <= numeros[0] <= 5) and (1 <= numeros[1] <= 5):
        print(sum(numeros))
    else:
        pass
        
