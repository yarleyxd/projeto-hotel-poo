from modelos.quarto import Quarto

class Standard(Quarto):
    def __init__(self, numero, capacidade, diaria_base, tipo_cama):
        super().__init__(numero, capacidade, diaria_base)
        self.tipo_cama = tipo_cama

    def calcular_diaria(self, noites):
        return self.diaria_base * noites
    
    def descrever_comodidades(self):
        return "Quarto Standard: cama de casal, banheiro e televisão."
    
    def descrever_quarto(self):
        return super().descrever_quarto() + f" | Cama: {self.tipo_cama}"

    def __str__(self):
        return super().__str__() + f" - Standard, cama {self.tipo_cama}"