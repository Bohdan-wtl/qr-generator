from base.base_page import BasePage


class LoginPageLocators:

    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        self.email_log_in = self.base.locator("//input[@id='input-email']")
        self.password_log_in = self.base.locator("//input[@id='input-password']")
        self.log_in_confirm_button = self.base.locator("//button[@id='login-btn']")
