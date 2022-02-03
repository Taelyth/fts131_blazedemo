# language: pt

Funcionalidade: Cadastro no site BlazeDemo
  Cenario: Cadastro válido com E-mail e Senha
    Dado que acesso o site BlazeDemo
    E clico no botão Home
    Quando clico no botão Register
    E preencho os dados cadastrais como "Teste teste", "Teste", "teste@teste.com.br", "123456"
    Então valido se foi feita a troca de página