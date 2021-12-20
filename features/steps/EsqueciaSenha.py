from behave import *
from selenium.webdriver.common.by import By


@when(u'clico no botão Forgot Your Password')
def clico_no_botao_forgot(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a.btn-link').click()


@when(u'preencho o email como "{email}"')
def preencho_o_email_como(context, email):
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Reset Password'
    context.driver.find_element(By.ID, 'email').send_keys(email)


@when(u'clico no botão Send Password Reset Link')
def clico_no_botao_send(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
