from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")

    def abrir(self):
        super().abrir(self.URL)
        return self

    def preencher_email(self, email):
        self.digitar(self.EMAIL_INPUT, email)

    def preencher_senha(self, senha):
        self.digitar(self.PASSWORD_INPUT, senha)

    def clicar_login(self):
        self.clicar(self.LOGIN_BUTTON)

    def fazer_login(self, username, password):
        self.preencher_email(username)
        self.preencher_senha(password)
        self.clicar_login()

    def obter_mensagem_erro(self):
        return self.obter_texto(self.ERROR_MESSAGE)

    def mensagem_erro_visivel(self):
        return self.esta_visivel(self.ERROR_MESSAGE, timeout=5)
