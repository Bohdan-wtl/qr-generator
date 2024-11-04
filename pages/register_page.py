from base.base_page import BasePage
from pages.locators.register_page_locators import RegisterPageLocators

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = RegisterPageLocators(page)


    def sign_up(self, temporary_mail, signup_password):
        self.locator.email_input_field.is_visible()
        self.locator.email_input_field.fill(temporary_mail)
        self.locator.password_input_field.fill(signup_password)
        self.locator.sign_up_confirm_button.click()