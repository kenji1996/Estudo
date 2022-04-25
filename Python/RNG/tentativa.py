class Configuracao:

    def __init__(self, n, t):
        self.n = n
        self.t = t

class Tentativa:

    def __init__(self, configuracao : Configuracao, n_gerado, n_escrito):
        self.configuracao = configuracao
        self.n_gerado = n_gerado
        self.n_escrito = n_escrito
        