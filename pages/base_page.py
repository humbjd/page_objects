from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self,driver):
        self.driver = driver # Este é o Selenium

    def _entrar(self,url):
        self.driver.get(url)

    def _encontrar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _clicar(self, locator):
        self._encontrar(locator).click()

    def _escrever(self, locator, text):
        self._encontrar(locator).send_keys(text)

    def _aparece(self, locator, timeout=1):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(
                    expected_conditions.visibity_of_element_located(
                        (locator['by']), locator['value']
                    )
                )
            except TimeoutException:
                return False
            return True # Como se estivesse dentro do try
        else:
            try:
                return self._encontrar(locator).is_displayed()
            except NoSuchElementException:
                return False





