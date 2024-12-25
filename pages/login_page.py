import allure

from base.base_page import BasePage
from pages.locators.login_page_locators import LoginPageLocators

class LogInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = LoginPageLocators(page)

    @allure.step("Perform user login process with email: {temporary_mail}")
    def log_in(self, temporary_mail, signup_password):
        with allure.step(f"Enter email address in login form: {temporary_mail}"):
            self.checked_locator(locator=self.locator.email_log_in).fill(temporary_mail)
        
        with allure.step("Proceed to password entry"):
            self.checked_locator(locator=self.locator.log_in_confirm_button).click()
        
        with allure.step("Enter password in login form"):
            self.checked_locator(locator=self.locator.password_log_in).fill(signup_password)
        
        with allure.step("Submit login credentials"):
            self.checked_locator(locator=self.locator.log_in_confirm_button).click()
