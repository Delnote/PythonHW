from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "login": ('ID', 'user-name'),
        "password": ('CSS', '[data-test="password"]'),
        "submit": ('XPATH', '//*[@type="submit"]')
        }

    def do_login(self):
        self.login.set_text("standard_user")
        self.password.set_text("secret_sauce")
        self.submit.click_button()
