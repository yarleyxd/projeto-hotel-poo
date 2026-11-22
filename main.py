from modelos.quarto import Quarto
from modelos.standard import Standard
from modelos.familia import Familia
from modelos.cobertura import Cobertura
from modelos.cafe_da_manha import CafeDaManha
from modelos.spa import Spa
from modelos.lavanderia import Lavanderia
from modelos.servico_extra import ServicoExtra

# Teste da classe Quarto (abstrata)
try:
    quarto = Quarto(101, 2, 150)
except TypeError as erro:
    print("Erro esperado ao instanciar Quarto:")
    print(erro)

# Teste da classe Standard
standard = Standard(102, 2, 180, "casal")

print("--- Quarto Standard ---")
print("Número:", standard.numero)
print("Capacidade:", standard.capacidade)
print("Diária:", standard.diaria_base)

print("Valor de 3 noites:", standard.calcular_diaria(3))
print(standard.descrever_comodidades())

# Teste das classes folha
quartos = [
    standard,
    Familia(103, 4, 250, 30),
    Cobertura(104, 5, 600, 150, True, 200)
]

print("--- Testando quartos ---")
for quarto in quartos:
    print(quarto)
    print("Valor de 3 noites:", quarto.calcular_diaria(3))
    print(quarto.descrever_comodidades())
    print("Descrição:", quarto.descrever_quarto())

# Teste de isistance()
print("--- Teste de herança ---")
for quarto in quartos:
    print(f"{quarto} é instância de Quarto:", isinstance(quarto, Quarto))

# Teste de serviços extras
print("\n--- Teste dos serviços extras ---")

servicos = [
    CafeDaManha(),
    Spa(),
    Lavanderia()
]

for servico in servicos:
    if isinstance(servico, ServicoExtra):
        print(servico.descricao())
        print("Custo: R$", servico.calcular_custo())