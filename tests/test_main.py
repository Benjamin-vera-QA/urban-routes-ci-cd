from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_python_org():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    assert "Python" in driver.title
    driver.quit()
