from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

def test_open_python_org():

    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument("--headless")  # Ejecuta sin ventana
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    driver.quit()
