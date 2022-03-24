class Cachorro:

    def __init__(self,nome = 'Desconhecido',pelo = 'Desconhecido',tamanho = 'Desconhecido',patas = 4):

        """Um jeito de usar construtor de uma classe:
        nome_variavel = Cachorros('nome','pelo','tamanho')
        15;03;2022 - Esse construtor é melhor pra manter o código mais claro. 
        Caso haja um tipo de estrutura de dado que seja mutavel (lista, etc)
        não é recomendado usar um valor padrão dentro do init pois este será
        compartilhado com TODAS as instâncias, ex: 

        >>> def __init__(self, name, subjects=["maths", "physics"]):
        >>>     self.name = name
        >>>     self.subjects = subjects
        >>> 
        >>> student0 = Student("John")
        >>> student0.subjects.append("music")
        >>> student0.subjects
        ['maths', 'physics', 'music']
        >>> student1 = Student("Ashley")
        >>> student1.subjects
        ['maths', 'physics', 'music']""" 

        self.nome = nome
        self.pelo = pelo
        self.tamanho = tamanho
        self.patas = patas

class Gato:
    alimento = 'carne'
    patas = '4'

    def __ini__(self, **kwargs):

        """ Outro jeito de fazer um construtor porem usar dicionario como argumento nao e recomendado 
            pois oculta quais parâmetros são necessários para a instância
            
            Also, pop() remove um elemento de um dicionário, então kwargs sendo um dicionário terá todos 
            os elementos removidos e transferidos para instância Gato"""
            
        self.alimento = kwargs.pop('alimento')
        self.patas = kwargs.pop('patas')

print(Cachorro.__init__.__doc__)