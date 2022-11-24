import time

from selenium import webdriver
from pages import *

base_url = 'https://www.demoblaze.com/'
# presented as mockup for robot

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)

    login.open_login_form()
    login.check_login_form()
    login.do_login()
    dashboard.check_logged_in()


def test_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    monitors_page = MonitorsPage(driver)
    products_page = ProductPage(driver)
    cart_page = CartPage(driver)

    login.open_login_form()
    login.do_login()
    dashboard.check_logged_in()
    dashboard.go_to_monitors()
    time.sleep(5)
    monitor = monitors_page.get_most_expensive_monitor()
    products_page.verify_product(monitor)
    products_page.add_to_cart()
    dashboard.go_to_cart()
    cart_page.verify_product(monitor)
