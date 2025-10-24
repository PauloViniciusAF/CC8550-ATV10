import os
import sys
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ensure project root is importable when pytest is invoked via the console script.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

@pytest.fixture
def chrome_driver():
    options = Options()

    # Hardening flags keep Chrome responsive inside containers/CI.
    flags = [
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
    ]
    for flag in flags:
        options.add_argument(flag)

    headless = os.getenv("SELENIUM_HEADLESS", "1").lower() not in {"0", "false", "no"}
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()
