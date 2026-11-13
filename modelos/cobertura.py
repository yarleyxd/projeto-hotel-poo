from modelos.suite import Suite


class Cobertura(Suite):
    def __init__(self, numero, capacidade, diaria_base, adicional_luxo, sala_estar, taxa_fixa):
        super().__init__(numero, capacidade, diaria_base, adicional_luxo, sala_estar)
        self.taxa_fixa = taxa_fixa

    def calcular_diaria(self, noites):
        return super().calcular_diaria(noites) + self.taxa_fixa

    def descrever_comodidades(self):
        return super().descrever_comodidades() + " Possui área exclusiva."