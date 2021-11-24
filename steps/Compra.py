from behave import *


def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )



@given(u'que acesso o site Blazedemo')
def que_acesso_o_site_blazedemo(context):
    print('Passo 1 - Abriu o site Blazedemo')
    # https://blazedemo.com/


@when(u'pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_sp_a_ny(context, origem, destino):
    print(f'Passo 2 - Pesquisou por passagem de {origem} a {destino}')


@when(u'seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    print('Passo 3 - Selecionou o primeiro voo')


@when(u'preencho os dados de pagamento como "{cartao}", "{titular}", "{validade}", "{cvv}"')
def preencho_os_dados_de_pagamento_como(context, cartao, titular, validade, cvv):
    cartoes = [row["cartao"] for row in context.table]
    print('Passo 4 - Preencheu os dados de pagamento como '
          f'{cartoes}, {titular}, {validade}, {cvv}')


@then(u'valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida(context):
    print('Passo 5 - Validou se a passagem foi emitida')
