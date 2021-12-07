from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# def before_feature(context, feature):
#     if 'compra_passagem' in feature.tag:
#         context.execute_steps(
#
#         )

# Atributos e variáveis dos


@given(u'que acesso o site Blazedemo')
def que_acesso_o_site_blazedemo(context):
    context.driver.get('https://blazedemo.com/')
    print('Passo 1 - Abriu o site Blazedemo')
    # https://blazedemo.com/


@when(u'pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_origem_destino(context, origem, destino):
    # Selecionar origem
    elemento_origem = context.driver.find_element(By.NAME, 'fromPort')
    objeto_origem = Select(elemento_origem)
    objeto_origem.select_by_visible_text(origem)

    # Selecionar destino
    elemento_destino = context.driver.find_element(By.NAME, 'toPort')
    objeto_destino = Select(elemento_destino)
    objeto_destino.select_by_visible_text(destino)

    # Clicar no botão de pesquisar voos
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn-primary').click()
    print(f'Passo 2 - Pesquisou por passagem de {origem} a {destino}')


@when(u'seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    context.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) input').click()
    print('Passo 3 - Selecionou o primeiro voo')


@when(u'preencho os dados de pagamento como "{cartao}", "{titular}", "{validade}", "{cvv}"')
def preencho_os_dados_de_pagamento_como(context, cartao, titular, validade, cvv):
    cartoes = [row["cartao"] for row in context.table]
    titulares = [row["titular"] for row in context.table]
    validades = [row["validade"] for row in context.table]
    cvvs = [row["cvv"] for row in context.table]

    context.driver.find_element(By.ID, 'inputName').send_keys('Fernando Vitor Moreira')
    context.driver.find_element(By.ID, 'address').send_keys('Iterasys')
    context.driver.find_element(By.ID, 'city').send_keys('São Paulo')
    context.driver.find_element(By.ID, 'state').send_keys('SP')
    context.driver.find_element(By.ID, 'zipCode').send_keys('012134-111')
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn-primary').click()

    print(f'Passo 4 - Preencheu os dados de pagamento como {cartoes}, {titulares}, {validades}, {cvvs}')


@then(u'valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida(context):
    assert context.driver.title == 'BlazeDemo Confirmation'
    print('Passo 5 - Validou se a passagem foi emitida')
