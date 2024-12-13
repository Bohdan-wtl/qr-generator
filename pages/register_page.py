import allure

from base.base_page import BasePage
from pages.locators.register_page_locators import RegisterPageLocators

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = RegisterPageLocators(page)


    @allure.step("Sign up")
    def sign_up(self, temporary_mail, signup_password):
        self.checked_locator(locator=self.locator.email_input_field).fill(temporary_mail)
        self.checked_locator(locator=self.locator.password_input_field).fill(signup_password)
        self.checked_locator(locator=self.locator.sign_up_confirm_button).click()