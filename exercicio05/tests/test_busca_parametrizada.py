import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.wikipedia.org")
    
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys(termo_busca)
    search_box.send_keys(Keys.ENTER)
    
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )
    
    assert termo_busca.lower() in heading.text.lower()
