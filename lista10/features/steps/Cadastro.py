from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@given(u'que acesso o site BlazeDemo')
def que_acesso_o_site_blazedemo(context):
    context.driver.get('https://blazedemo.com/')
    print('Passo 1 - Abriu o site Blazedemo')
    # https://blazedemo.com/


@given(u'clico no botão Home')
def clico_no_botao_home(context):
    context.driver.find_element(By.LINK_TEXT, 'home').click()
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Login'
    print(f'Passo 2 - Clicou no botao Home')


@when(u'clico no botão Register')
def clico_no_botao_register(context):
    context.driver.find_element(By.LINK_TEXT, 'Register').click()
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Register'
    print(f'Passo 3 - Clicou no botao Register')


@when(u'preencho os dados cadastrais como "{name}", "{company}", "{email}", "{password}"')
def preencho_dados_cadastrais_como(context, name, company, email, password):

    context.driver.find_element(By.ID, 'name').send_keys(name)
    context.driver.find_element(By.ID, 'company').send_keys(company)
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'password-confirm').send_keys(password)

    context.driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

    print('Passo 4 - Preencheu os dados cadastrais como '
          f'{name}, {company}, {email}, {password}')


@then(u'valido se foi feita a troca de página')
def valido_se_foi_feita_a_troca_de_pagina(context):
    try:
        assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
        assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    except NoSuchElementException:
        print('deu ruim')

    print('Passo 5 - Validou a troca de página')
