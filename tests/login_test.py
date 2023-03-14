import os

import pytest


@pytest.fixure
def login(request):
    # variavel local para armazenar o caminho do ChromeDriver
    _chromedriver = os.path.join(os.getcwd(),'vendor', 'chromedriver.exe')

    if os.path.isfile(_chromedriver):
        driver_