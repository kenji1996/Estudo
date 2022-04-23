resto = 0
multiplier = 1
valor_numero = []
valores_possiveis = []

def a(numero,a,b):
    todos_valores = []
    aux = 5
    if isinstance(b,list) and len(b) > 1:
        for i in b:
            if all(i=='1' or i=='0' for i in str(b)):
                return numero, a, b

    if len(a) == 0 and len(b) == 0:
        for i in range(1,10,1):
            o = int(numero[len(numero)-1]) * i % 10
            if o == 1 or o == 0:
                lista_digitos,lista_valores = [],[]
                lista_digitos.append(i)
                lista_valores.append(int(numero[len(numero)-1]) * i)
    else:
        




def multiplo(numero, num_anterior = None, digitos = ""):
    #check if number is already okay
    if all(i=='0' or i=='1' for i in str(numero)):
        return num_anterior
        """ numero *= num_anterior
        numero = int(str(numero[:-1])) """
    if isinstance(num_anterior, list) and len(num_anterior) != 0:
            for i in num_anterior:
                digitos = numero * i
                digitos = int(str(numero[:-1]))

        multiplo(numero)
    valores = []
    multiplier = 1
    aux = 5
    if num_anterior == None:
        for i in range(1,10,1):
            aux = (i * numero) % 10
            if aux == 1 or aux == 0:
                valores.append(i)
    else:
        for i in range(0,10,1):
            aux = (i * numero) % 10
            if aux == 1 or aux == 0:
                valores.append(i)   

    return valores

a = multiplo(143)
print(a)