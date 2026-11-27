from abc import ABC, abstractmethod

class Quarto(ABC):
    def __init__(self, numero, capacidade, diaria_base):
        self.numero = numero
        self.capacidade = capacidade
        self.diaria_base = diaria_base
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("O número do quarto deve ser um inteiro positivo.")
        self._numero = valor
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, valor):
        if not isinstance(valor, int) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("A capacidade deve ser um inteiro positivo.")
        self._capacidade = valor

    @property
    def diaria_base(self):
        return self._diaria_base

    @diaria_base.setter
    def diaria_base(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor < 0:
            raise ValueError("A diária base deve ser um número maior ou igual a zero.")
        self._diaria_base = valor
    
    @property
    def tipo_quarto(self):
        """Propriedade somente leitura"""
        return self.__class__.__name__

    @property
    def valor_diaria(self):
        """Valor calculado para uma noite considerando a classe concreta"""
        return self.calcular_diaria(1)

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