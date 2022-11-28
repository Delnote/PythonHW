import time

import pytest

from pages import *
from constants import *


class Tests:

    def test_login(cls):
        login = LoginPage(cls.driver)
        dashboard = DashboardPage(cls.driver)
        login.open_login_form()
        login.check_login_form()
        login.do_login()
        dashboard.check_logged_in()

    def test_cart(cls):
        login = LoginPage(cls.driver)
        dashboard = DashboardPage(cls.driver)
        monitors_page = MonitorsPage(cls.driver)
        products_page = ProductPage(cls.driver)
        cart_page = CartPage(cls.driver)

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
