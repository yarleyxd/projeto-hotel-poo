from abc import ABC, abstractmethod

class Quarto(ABC):
    def __init__(self, numero, capacidade, diaria_base):
        self.numero = numero
        self.capacidade = capacidade
        self.diaria_base = diaria_base
    
    @abstractmethod
    def calcular_diaria(self, noites):
        pass
    
    @abstractmethod
    def descrever_comodidades(self):
        pass

    def descrever_quarto(self):
        return (
            f"Quarto {self.numero} |"
            f"Capacidade: {self.capacidade} pessoas |"
            f"Diária base: R$ {self.diaria_base:.2f}"
        )
    
    def __str__(self):
        return f"Quarto {self.numero} (R$ {self.diaria_base:.2f})"