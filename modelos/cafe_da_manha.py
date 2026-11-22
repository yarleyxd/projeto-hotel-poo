from modelos.servico_extra import ServicoExtra


class CafeDaManha(ServicoExtra):

    def descricao(self):
        return "Cafe da manha incluso."

    def calcular_custo(self):
        return 30