from modelos.quarto import Quarto


class Familia(Quarto):
    def __init__(self, numero, capacidade, diaria_base, adicional_por_pessoa):
        super().__init__(numero, capacidade, diaria_base)
        self.adicional_por_pessoa = adicional_por_pessoa

    @property
    def adicional_por_pessoa(self):
        return self._adicional_por_pessoa
    
    @adicional_por_pessoa.setter
    def adicional_por_pessoa(self,valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("O adicional por pessoa deve ser maior ou igual a zero")
        self._adicional_por_pessoa = valor
    
    @property
    def valor_diaria(self):
        return self.diaria_base + self.adicional_por_pessoa * self.capacidade

    def calcular_diaria(self, noites):
        return (
            self.diaria_base * noites
            + self.adicional_por_pessoa * self.capacidade * noites
        )

    def descrever_comodidades(self):
        return "Quarto Família: camas extras e espaço para família."