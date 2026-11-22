# Sistema de Gerenciamento de Hotel

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos (POO).

## Integrantes

- Carlos Ítalo Alves Ferreira
- Yarley Aguiar de Sousa
- Vinícius Maia Silva

## Objetivo

Desenvolver um sistema para modelagem de quartos de hotel utilizando conceitos fundamentais de Programação Orientada a Objetos.

## Estrutura de Classes

O sistema possui uma hierarquia de classes baseada na classe principal `Quarto`.

### Hierarquia

```text
Quarto
├── Standard
├── Familia
└── Luxo
    └── Suite
        └── Cobertura
```

## Conceitos de POO Aplicados

### Herança

As classes Standard, Familia e Luxo herdam da classe Quarto. As classes Suite e Cobertura herdam de classes especializadas, formando uma hierarquia multinível.

### Polimorfismo

Os métodos `calcular_diaria()` e `descrever_comodidades()` são redefinidos nas subclasses para comportamentos específicos.

### Encapsulamento

Os atributos de cada classe são armazenados internamente e manipulados pelos métodos dos objetos.

## Arquivos

- quarto.py
- standard.py
- familia.py
- luxo.py
- suite.py
- cobertura.py

## Diagrama UML

Consulte o arquivo `diagrama.md`.

## Tecnologias

- Python 3
- Git
- GitHub
- Visual Studio Code

### Classe Abstrata

A classe abstrata `Quarto` possui os métodos abstratos `calcular_diaria()` e `descrever_comodidades()`.

As classes `Standard`, `Familia` e `Luxo` implementam esses métodos. `Suite` e `Cobertura` herdam os métodos implementados.

### Interface

A interface `ServicoExtra` possui os métodos `descricao()` e `calcular_custo()`.

As classes `CafeDaManha`, `Spa` e `Lavanderia` implementam essa interface.

### Testes

O `main.py` demonstra o erro ao tentar instanciar a classe abstrata `Quarto`, utiliza os métodos polimórficos nas classes de quartos e utiliza `isinstance()` para verificar os serviços extras.