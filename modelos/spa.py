from modelos.servico_extra import ServicoExtra


class Spa(ServicoExtra):

    def descricao(self):
        return "Acesso ao spa do hotel."

    def calcular_custo(self):
        return 80