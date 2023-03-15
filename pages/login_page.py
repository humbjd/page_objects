# 1 -  Bibliotecas
from selenium.webdriver.common.by import By


# 2 - Classe

class LoginPage():
    # 2.1 - Mapeamento dos Elementos da Classe
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}

   # 2.2 - Inicializador / Construtor (Java)
    def __init__(self, driver):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def with_(self, username, password):
        self.driver.find_element(self._username_input['by':],
                                 self._username_input['value']).send_keys(username)

   # 2.3 - Ações Realizáveis


