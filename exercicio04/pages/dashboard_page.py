from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    SUCCESS_HEADING = (By.XPATH, "//h1[contains(normalize-space(),'Logged In Successfully')]")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".post-content p")

    def esta_logado(self):
        return self.esta_visivel(self.SUCCESS_HEADING, timeout=5)

    def obter_mensagem_boas_vindas(self):
        if self.esta_visivel(self.WELCOME_MESSAGE, timeout=5):
            return self.obter_texto(self.WELCOME_MESSAGE)
        return ""
