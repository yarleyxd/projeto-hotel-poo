from modelos.quarto import Quarto


class Luxo(Quarto):
    def __init__(self, numero, capacidade, diaria_base, adicional_luxo):
        super().__init__(numero, capacidade, diaria_base)
        self.adicional_luxo = adicional_luxo

    def calcular_diaria(self, noites):
        return super().calcular_diaria(noites) + self.adicional_luxo * noites

    def descrever_comodidades(self):
        return "Quarto Luxo: ar-condicionado, frigobar e hidromassagem."