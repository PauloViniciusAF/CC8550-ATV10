import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Site para o teste de login
URL = "https://practicetestautomation.com/practice-test-login/"

#Chrome Driver 
@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit()

@pytest.fixture
def open_login_page(chrome_driver):
    chrome_driver.get(URL)
    return chrome_driver

#Teste de login com sucesso
def test_login_sucesso(open_login_page):
    driver = open_login_page
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    assert "Logged In Successfully" in driver.page_source

#Teste de login com username inválido
def test_login_user_invalido(open_login_page):
    driver = open_login_page
    driver.find_element(By.ID, "username").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Your username is invalid!" in error

#Teste de login com senha inválida
def test_login_senha_incorreta(open_login_page):
    driver = open_login_page
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "submit").click()
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Your password is invalid!" in error

#Teste de login com campos vazios
def test_login_campos_vazios(open_login_page):
    driver = open_login_page
    driver.find_element(By.ID, "submit").click()
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Your username is invalid!" in error

#Teste de login com username e senha incorretos
def test_login_mensagem_erro_apropriada(open_login_page):
    driver = open_login_page
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    ).text
    assert "Your username is invalid!" in error