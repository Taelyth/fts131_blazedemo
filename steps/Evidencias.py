from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


def tirar_print_e_salvar(driver, nome):
    #datahora = datetime.now().strftime('%Y-%m-%d-%H-%M')
    datahora = datetime.now().strftime('%Y-%m-%d')
    Path(f'../prints/{datahora}').mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(f'../prints/{datahora}/{nome}.png')


def testar_blazedemo():
    driver = webdriver.Chrome('C:\\webdrivers\\chromedriver\\96\\chromedriver.exe')
    driver.get('https://www.blazedemo.com/')
    tirar_print_e_salvar(driver, 'home')
    driver.find_element(By.CSS_SELECTOR, 'input.btn-primary').click()
    tirar_print_e_salvar(driver, 'voos')
    driver.quit()
