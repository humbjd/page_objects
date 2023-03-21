#import os
import pytest
#from selenium import webdriver
from pages import login_page

@pytest.fixture
def login(driver): # Deixou de receber request e recebe diretamente driver
    return login_page.LoginPage(driver)  # Instanciando a classe LoginPage e passando o Selenium

def testar_login_com_sucesso(login):
    # Preencher o usuário, a senha e clicar no botão
    login.com_('tomsmith', 'SuperSecretPassword!')
    # Validar a mensagem
    assert login.vejo_mensagem_de_sucesso()

def testar_login_com_usuario_invalido(login):
    # Preencher o usuário, a senha e clicar no botão
    login.com_('asdfgasdfg', 'SuperSecretPassword!')
    # Validar a mensagem
    assert login.vejo_mensagem_de_falha()

def testar_login_com_senha_invalida(login):
    # Preencher o usuário, a senha e clicar no botão
    login.com_('tomsmith', 'xpto12345')
    # Validar a mensagem
    assert login.vejo_mensagem_de_falha()