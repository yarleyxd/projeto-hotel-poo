from modelos.luxo import Luxo


class Suite(Luxo):
    def __init__(self, numero, capacidade, diaria_base, adicional_luxo, sala_estar):
        super().__init__(numero, capacidade, diaria_base, adicional_luxo)
        self.sala_estar = sala_estar

    def calcular_diaria(self, noites):
        return super().calcular_diaria(noites)

    def descrever_comodidades(self):
        return super().descrever_comodidades() + " Possui sala de estar."