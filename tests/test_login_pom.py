import pytest

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(chrome_driver):
    return LoginPage(chrome_driver).abrir()


def test_login_sucesso_pom(login_page):
    login_page.fazer_login("student", "Password123")
    dashboard = DashboardPage(login_page.driver)

    assert dashboard.esta_logado()
    mensagem = dashboard.obter_mensagem_boas_vindas()
    assert mensagem and "successfully" in mensagem.lower()


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("usuario_invalido", "Password123", "Your username is invalid!"),
        ("student", "senha_errada", "Your password is invalid!"),
    ],
)
def test_login_credenciais_invalidas_pom(login_page, username, password, expected_error):
    login_page.fazer_login(username, password)
    assert login_page.mensagem_erro_visivel()
    assert expected_error in login_page.obter_mensagem_erro()


def test_login_campos_vazios_pom(login_page):
    login_page.clicar_login()
    assert login_page.mensagem_erro_visivel()
    assert "Your username is invalid!" in login_page.obter_mensagem_erro()
