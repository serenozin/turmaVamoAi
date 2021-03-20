class Cachorro:
    def __init__(self, nome, cor, quant_patas, raca, porte):
        self.nome = nome
        self.cor = cor
        self.quant_patas = quant_patas
        self.raca = raca
        self.porte = porte 

    def comer(self, racao):
        self.racao = racao

    def dormir(self, lugar):
        self.lugar = lugar

    def latir(self, gatilho):
        self.gatilho = gatilho

    def coco(self, lugar):
        self.lugar = lugar

    def xixi(self, lugar):
        self.lugar = lugar

        