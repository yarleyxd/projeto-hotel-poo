from modelos.quarto import Quarto
from modelos.standard import Standard
from modelos.familia import Familia
from modelos.cobertura import Cobertura

# Teste da classe Quarto
quarto = Quarto(101, 2, 150)

print("Número:", quarto.numero)
print("Capacidade:", quarto.capacidade)
print("Diária:", quarto.diaria_base)

print("Valor de 3 noites:", quarto.calcular_diaria(3))
print(quarto.descrever_comodidades())

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

for quarto in quartos:
    print(quarto)
    print("Valor de 3 noites:", quarto.calcular_diaria(3))
    print(quarto.descrever_comodidades())

print(isinstance(quartos[0], Quarto))