import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixure
def login(request):
    # variavel local para armazenar o caminho do ChromeDriver
    _chromedriver = os.path.join(os.getcwd(),'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        # se existe um chromedriver dentro do projeto, instancie com ele
        driver_ = webdriver.Chrome(_chromedriver) # ligando o Selenium
    else:
        # se nao existe, tente usar um chromedriver publico no ambiente
        driver_ = webdriver.Chrome()

    def quit():
        driver_.quit() # desligar o Selenium

    # sinalizando o fim da execução para o ambiente
    request.addfinalizer(quit)
    return driver_

def test_login_valido(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

