# 1 -  Bibliotecas
from selenium.webdriver.common.by import By
from pages.base_page import BasePage # receber as funções da base_page

# 2 - Classe

class LoginPage(BasePage):
    # 2.1 - Mapeamento dos Elementos da Classe
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _sucess_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.sucess'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}

# Erro: Descoberto pelo próprio autor
# Defeito: Descoberto de forma estática por outra pessoa
# Falha: Descoberta de forma dinâmica por outra pessoa

   # 2.2 - Inicializador / Construtor (Java)
    def __init__(self, driver):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def com_(self, username, password):
        self.driver.find_element(self._username_input['by'],
                                 self._username_input['value']).send_keys(username)
        self.driver.find_element(self._password_input['by'],
                                 self._password_input['value']).send_keys(password)
        self.driver.find_element(self._login_button['by'],
                                 self._login_button['value']).click()

   # 2.3 - Ações Realizáveis
    def vejo_mensagem_de_sucesso(self):
        return self.driver.find_element(self._sucess_message['by'],
                                 self._sucess_message['value']).is_displayed()

    def vejo_mensagem_de_falha(self):
        return self.driver.find_element(self._failure_message['by'],
                                        self._failure_message['value']).is_displayed()

