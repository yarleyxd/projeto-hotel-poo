from modelos.servico_extra import ServicoExtra


class Lavanderia(ServicoExtra):

    def descricao(self):
        return "Servico de lavanderia."

    def calcular_custo(self):
        return 25