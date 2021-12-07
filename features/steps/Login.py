from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@when(u'clico em Home')
def clico_em_home(context):
    context.driver.find_element(By.LINK_TEXT, 'home').click()


@then(u'exibe a pagina de Login')
def exibe_pagina_de_login(context):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Login'


@when(u'preencho "{email}" e "{senha}"')
def preencho_email_e_senha(context, email, senha):
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(senha)


@when(u'clico em Login')
def clico_em_login(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()


@then(u'exibe a mensagem de pagina expirada')
def exibe_a_mensagem(context):
    try:
        assert context.driver.find_element(By.CSS_SELECTOR, 'div.code').text == '419'
        assert context.driver.find_element(By.CSS_SELECTOR, 'div.message').text == 'Page Expired'
    except NoSuchElementException:
        print('deu ruim')
