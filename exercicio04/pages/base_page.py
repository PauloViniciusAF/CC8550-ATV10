from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait_time = wait_time

    def abrir(self, url):
        self.driver.get(url)

    def _esperar(self, locator, condition=EC.presence_of_element_located):
        return WebDriverWait(self.driver, self.wait_time).until(condition(locator))

    def localizar(self, locator):
        return self._esperar(locator)

    def digitar(self, locator, texto):
        element = self._esperar(locator, condition=EC.visibility_of_element_located)
        element.clear()
        element.send_keys(texto)
        return element

    def clicar(self, locator):
        element = self._esperar(locator, condition=EC.element_to_be_clickable)
        element.click()
        return element

    def obter_texto(self, locator):
        element = self._esperar(locator, condition=EC.visibility_of_element_located)
        return element.text

    def esta_visivel(self, locator, timeout=None):
        wait_time = timeout or self.wait_time
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
