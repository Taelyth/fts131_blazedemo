# language: pt

@compra_passagem
Funcionalidade: Compra de Passagem Aerea
#  Cenario: Viagem de Sao Paulo a New York
#    Dado que acesso o site Blazedemo
#    Quando pesquiso passagens de "São Paolo" a "New York"
#    E seleciono o primeiro voo
#    E preencho os dados de pagamento como "<cartao>", "<titular>", "<validade>", "<cvv>"
#      | cartao              | titular                   | validade | cvv |
#      | 5229 9718 5701 6600 | Fernando Vitor Moreira    | 06/22    | 467 |
#      | 4485 7861 1750 8440 | Sophia Teresinha Baptista | 05/23    | 667 |
#    Entao valido se a passagem foi emitida
#
#  Cenario: Viagem de Boston a Dublin
#    Dado que acesso o site Blazedemo
#    Quando pesquiso passagens de "Boston" a "Dublin"
#    E seleciono o primeiro voo
#    E preencho os dados de pagamento como "<cartao>", "<titular>", "<validade>", "<cvv>"
#      | cartao              | titular                | validade | cvv |
#      | 5229 9718 5701 6600 | Fernando Vitor Moreira | 06/22    | 467 |
#    Entao valido se a passagem foi emitida

  Esquema do Cenario: Compra de Passagens
    Dado que acesso o site Blazedemo
    Quando pesquiso passagens de "<origem>" a "<destino>"
    E seleciono o primeiro voo
    E preencho os dados de pagamento como "<cartao>", "<titular>", "<validade>", "<cvv>"
      | cartao              | titular                | validade | cvv |
      | 5229 9718 5701 6600 | Fernando Vitor Moreira | 06/22    | 467 |
    Entao valido se a passagem foi emitida
    Exemplos: Locais
      | origem      | destino      |
      | Paris       | Buenos Aires |
      | Mexico City | Rome         |