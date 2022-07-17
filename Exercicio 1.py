class VotosEleicoes():

    def __init__(self, totalvotos, validos, brancovotos, nulos):
        self.totalvotos = totalvotos
        self.validos = validos
        self.brancovotos = brancovotos
        self.nulos = nulos
    def votos_validos(self):
        var = self.validos / self.totalvotos
        print('{:.0%}'.format(var))
    def votos_brancos(self):
        var = self.brancovotos / self.totalvotos
        print('{:.0%}'.format(var))
    def votos_nulos(self):
        var = self.nulos / self.totalvotos
        print('{:.0%}'.format(var))


#Programa

total_de_votos = VotosEleicoes(1000,800,150,50)

total_de_votos.votos_validos()
total_de_votos.votos_brancos()
total_de_votos.votos_nulos()