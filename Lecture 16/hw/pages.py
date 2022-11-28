from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory
from constants import *


class LoginPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "login_button": ('ID', 'login2'),
        "login": ('ID', 'loginusername'),
        "password": ('ID', 'loginpassword'),
        "submit": ('XPATH', '//button[.=\'Log in\']')
    }

    def open_login_form(self):
        self.login_button.click()

    def check_login_form(self):
        assert self.login.is_displayed()
        assert self.password.is_displayed()
        assert self.submit.is_displayed()

    def do_login(self):
        self.login.set_text(LOGIN)
        self.password.set_text(PASSWORD)
        self.submit.click()


class DashboardPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "logout_button": ('ID', 'logout2'),
        "wellcome_text": ('ID', 'nameofuser'),
        "monitors": ('XPATH', '//*[.=\'Monitors\']'),
        "cart": ('ID', 'cartur')
    }

    def check_logged_in(self):
        assert self.logout_button.is_displayed()
        assert self.wellcome_text.text == 'Welcome usertesttest'

    def go_to_monitors(self):
        self.monitors.click()

    def go_to_cart(self):
        self.cart.click()


class MonitorsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def get_most_expensive_monitor(self) -> {}:
        prod_data = {}

        elems = self.driver.find_elements(By.CSS_SELECTOR, "[id='tbodyid'] div div.card")
        max_index = max(e.find_element(By.CSS_SELECTOR, 'h5').text for e in elems)
        monitor = self.driver.find_element(By.XPATH, '//h5[.=\'' + max_index + '\']/../..')

        prod_data.__setitem__('name', monitor.find_element(By.CSS_SELECTOR, 'h4.card-title').text)
        prod_data.__setitem__('price', monitor.find_element(By.CSS_SELECTOR, 'h5').text)

        self.driver.find_element(By.XPATH, '//h5[.=\'' + max_index + '\']/..//a').click()
        return prod_data


class ProductPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "product_name": ('CSS', 'h2.name'),
        "product_price": ('CSS', 'h3.price-container'),
        "submit_to_cart": ('XPATH', '//a[.=\'Add to cart\']')
    }

    def verify_product(self, product: {}):
        assert self.product_name.text == product.__getitem__('name')
        assert product.__getitem__('price') in self.product_price.text

    def add_to_cart(self):
        self.submit_to_cart.click()


class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "product_name": ('CSS', '.success td:nth-child(2)'),
        "product_price": ('CSS', '.success td:nth-child(3)')
    }

    def verify_product(self, product: {}):
        assert self.product_name.text == product.__getitem__('name')
        assert self.product_price.text in product.__getitem__('price')
