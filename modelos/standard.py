from modelos.quarto import Quarto

class Standard(Quarto):
    def __init__(self, numero, capacidade, diaria_base):
        super().__init__(numero, capacidade, diaria_base)

    def calcular_diaria(self, noites):
        return super().calcular_diaria(noites)
    
    def descrever_comodidades(self):
        return "Quarto Standard: cama de casal, banheiro e televisão."