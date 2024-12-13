import allure

from base.base_page import BasePage
from pages.locators.login_page_locators import LoginPageLocators

class LogInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = LoginPageLocators(page)

    @allure.step("Log in")
    def log_in(self, temporary_mail, signup_password):
        self.checked_locator(locator=self.locator.email_log_in).fill(temporary_mail)
        self.checked_locator(locator=self.locator.log_in_confirm_button).click()
        self.checked_locator(locator=self.locator.password_log_in).fill(signup_password)
        self.checked_locator(locator=self.locator.log_in_confirm_button).click()
