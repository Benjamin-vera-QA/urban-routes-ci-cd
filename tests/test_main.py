from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_python_org():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    driver.quit()
