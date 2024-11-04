from base.base_page import BasePage
from pages.locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = AccountPageLocators(page)

    def log_out_from_active_session(self):
        self.locator.log_out_button.click()

    def password_update(self, signup_password):
        self.locator.password_update_input.fill(signup_password)
        self.locator.password_update_confirm_input.fill(signup_password)
        self.locator.password_update_submit_button.click()