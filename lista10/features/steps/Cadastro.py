from behave import *


@given(u'que acesso o site BlazeDemo')
def que_acesso_o_site_blazedemo(context):
    print('Passo 1 - Abriu o site Blazedemo')
    # https://blazedemo.com/


@given(u'clico no botão "{home}"')
def clico_no_botao_home(context, home):
    print(f'Passo 2 - Clicou no botao {home}')


@when(u'clico no botão "{register}"')
def clico_no_botao_register(context, register):
    print(f'Passo 3 - Clicou no botao {register}')


@when(u'preencho os dados cadastrais como "{name}", "{company}", "{email}", "{password}"')
def preencho_dados_cadastrais_como(context, name, company, email, password):
    print('Passo 4 - Preencheu os dados cadastrais como '
          f'{name}, {company}, {email}, {password}')


@then(u'valido se foi feita a troca de página')
def valido_se_foi_feita_a_troca_de_pagina(context):
    print('Passo 5 - Validou a troca de página')
