from modelos.quarto import Quarto


class Familia(Quarto):
    def __init__(self, numero, capacidade, diaria_base, adicional_por_pessoa):
        super().__init__(numero, capacidade, diaria_base)
        self.adicional_por_pessoa = adicional_por_pessoa

    def calcular_diaria(self, noites):
        return super().calcular_diaria(noites) + self.adicional_por_pessoa * self.capacidade * noites

    def descrever_comodidades(self):
        return "Quarto Família: camas extras e espaço para família."