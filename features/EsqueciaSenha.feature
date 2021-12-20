# language: pt
@esqueceu_a_senha
Funcionalidade: Cadastro no site BlazeDemo
  Cenario: Cadastro válido com E-mail e Senha
    Dado que acesso o site BlazeDemo
    Quando clico em Home
    Então exibe a pagina de Login
    Quando clico no botão Forgot Your Password
    E preencho o email como "teste@teste.com.br"
    E clico no botão Send Password Reset Link
    Então exibe a mensagem de pagina expirada
