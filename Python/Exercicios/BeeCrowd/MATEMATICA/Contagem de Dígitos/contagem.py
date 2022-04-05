#entre invervalo X e Y, saber quantas vezes os digitos de 1 a 9 foram usados
import sys

contagem = [0] * 10

while True:
    try:
        x,y = input().split()
        x,y = int(x),int(y)
        if x and y == 0:
            sys.exit()
        for i in range(x,y+1,1):
            a = str(i)
            for o in a:
                contagem[int(o)] += 1
        print([i for i in contagem])
        contagem = [0] * 10
    except:
        pass

