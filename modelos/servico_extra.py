from abc import ABC, abstractmethod


class ServicoExtra(ABC):

    @abstractmethod
    def descricao(self):
        pass

    @abstractmethod
    def calcular_custo(self):
        pass