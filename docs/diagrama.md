# Diagrama UML

```mermaid
classDiagram

class Quarto{
    <<abstract>>
    +numero
    +capacidade
    +diaria_base
    +calcular_diaria(noites)*
    +descrever_comodidades()*
    +descrever_quarto()
    +__str__()
}

class ServicoExtra{
    <<interface>>
    +descricao()*
    +calcular_custo()*
}

class Standard{
    +tipo_cama
}

class Familia{
    +adicional_por_pessoa
}

class Luxo{
    +adicional_luxo
}

class Suite{
    +sala_estar
}

class Cobertura{
    +taxa_fixa
}

class CafeDaManha

class Spa

class Lavanderia

Quarto <|-- Standard
Quarto <|-- Familia
Quarto <|-- Luxo
Luxo <|-- Suite
Suite <|-- Cobertura

ServicoExtra <|.. CafeDaManha
ServicoExtra <|.. Spa
ServicoExtra <|.. Lavanderia