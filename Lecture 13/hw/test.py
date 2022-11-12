from selenium import webdriver
from loginpage import LoginPage

base_url = 'https://www.saucedemo.com/'


def test_login():
    expected_url = 'https://www.saucedemo.com/inventory.html'

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    login = LoginPage(driver)
    login.do_login()
    current_url = driver.current_url
    assert current_url == expected_url
