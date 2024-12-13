from base.base_page import BasePage


class RegisterPageLocators:
    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        self.email_input_field = self.base.locator("//input[@id='input-email']")
        self.password_input_field = self.base.locator("//input[@id='input-password']")
        self.sign_up_confirm_button = self.base.locator("//button[@type='submit']")