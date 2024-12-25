import allure

from base.base_page import BasePage
from pages.locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = AccountPageLocators(page)

    @allure.step("Sign out from current user session")
    def log_out_from_active_session(self):
        with allure.step("Click logout button"):
            self.checked_locator(locator=self.locator.log_out_button).click()

    @allure.step("Update account password")
    def password_update(self, signup_password):
        with allure.step("Enter new password"):
            self.checked_locator(locator=self.locator.password_update_input).fill(signup_password)
        with allure.step("Confirm new password"):
            self.checked_locator(locator=self.locator.password_update_confirm_input).fill(signup_password)
        with allure.step("Submit password update"):
            self.checked_locator(locator=self.locator.password_update_submit_button).click()