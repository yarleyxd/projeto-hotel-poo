class Quarto:
    def __init__(self, numero, capacidade, diaria_base):
        self.numero = numero
        self.capacidade = capacidade
        self.diaria_base = diaria_base
    
    def calcular_diaria(self, noites):
        return self.diaria_base * noites
    
    def descrever_comodidades(self):
        return "Quarto com comodidades básicas."

    def __str__(self):
        return f"Quarto {self.numero} (R$ {self.diaria_base:.2f})"