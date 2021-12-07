# language: pt

Funcionalidade: Login
  Cenario: Login Positivo
    Dado que acesso o site Blazedemo
    Quando clico em Home
    Então exibe a pagina de Login
    Quando preencho "teste@teste.com.br" e "123456"
    E clico em Login
    Então exibe a mensagem de pagina expirada