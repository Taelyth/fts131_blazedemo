from behave import when, then
from selenium.webdriver.common.by import By


@when(u'clico em The Beach!')
def clico_em_the_beach(context):
    context.driver.find_element(By.LINK_TEXT, 'destination of the week! The Beach!').click()


@then(u'vejo a promoção da semana')
def vejo_a_promocao_da_semana(context):
    texto_seletor = context.driver.find_element(By.CSS_SELECTOR, 'div.container:nth-child(2)').text
    assert texto_seletor == 'Destination of the week: Hawaii !'
    imagem_seletor = context.driver.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
    # assert imagem_seletor == 'https://blazedemo.com/assets/vacation.jpg'
    assert '/assets/vacation.jpg' in imagem_seletor
