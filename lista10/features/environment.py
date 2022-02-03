from selenium import webdriver


# Bloco executado antes de tudo - 1º a rodar
def before_all(context):
    # Declaramos o objeto do Selenium e o instanciamos como controlador do Chrome
    context.driver = webdriver.Chrome("C:\\webdrivers\\chromedriver\\96\\chromedriver.exe")
    context.driver.maximize_window()


# Bloco executado no final de tudo - Ultimo a rodar
def after_all(context):
    context.driver.quit()
