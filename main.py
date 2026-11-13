from modelos.quarto import Quarto
from modelos.standard import Standard

# Teste da classe Quarto
quarto = Quarto(101, 2, 150)

print("Número:", quarto.numero)
print("Capacidade:", quarto.capacidade)
print("Diária:", quarto.diaria_base)

print("Valor de 3 noites:", quarto.calcular_diaria(3))
print(quarto.descrever_comodidades())

# Teste da classe Standard
standard = Standard(102, 2, 180)

print("--- Quarto Standard ---")
print("Número:", standard.numero)
print("Capacidade:", standard.capacidade)
print("Diária:", standard.diaria_base)

print("Valor de 3 noites:", standard.calcular_diaria(3))
print(standard.descrever_comodidades())