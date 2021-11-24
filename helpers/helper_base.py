from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HelperFunc(object):
    __TIMEOUT = 10  # Definimos um limite de espera de 10 segundos

    # Definição de uma espera explícita
    def __init__(self, driver):  # Criou a Definição de inicialização da classe

        # Estabelece que driver herda de HelperFunc (pra chamar o driver de forma mais rápida):
        super(HelperFunc, self).__init__(driver)  # Também pode ser -> super().__init__(driver)

        # Criação de um objeto (_driver_wait) para controlar as esperas do Selenium (driver)
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

    # Definição da abertura de uma URL / Acessar um site
    def open(self, url):
        self._driver.get(url)

    # Maximizar a janela do browser
    def maximize(self):
        self._driver.maximize_window()

    # Finalizar o objeto do Selenium Webdriver
    def quit(self):
        self._driver.quit()

    # Definições úteis para selecionar elementos
    def seletor(self, by, seletor):
        try:
            if by == 'id':
                self._driver_wait.until(EC.visibility_of_element_located).find_element(By.ID, seletor)
            elif by == 'css':
                self._driver_wait.until(EC.visibility_of_element_located).find_element(By.CSS_SELECTOR, seletor)
            elif by == 'name':
                self._driver_wait.until(EC.visibility_of_element_located).find_element(By.CLASS_NAME, seletor)
            elif by == 'link':
                self._driver_wait.until(EC.visibility_of_element_located).find_element(By.LINK_TEXT, seletor)
            elif by == 'xpath':
                self._driver_wait.until(EC.visibility_of_element_located).find_element(By.XPATH, seletor)
        except Exception as EX:
            print(f'{EX}: By não definido')
        return self
