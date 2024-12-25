import allure

from base.base_page import BasePage
from pages.locators.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = AdminPageLocators(page)

    @allure.step("Open menu options for user '{user_email}' in Users tab")
    def get_user_menu_dots_button_users_tab(self, user_email):
        return self.page.locator(
            f"//tr[td//a[contains(text(), '{user_email}')]]//div[contains(@class, 'dropdown')]//button"
        )

    @allure.step("Open menu options for payment from user '{email_dpf}' in Payments tab")
    def get_user_menu_dots_button_payments_tab(self, email_dpf):
        return self.page.locator(
            f"//tr[.//span[contains(text(),'{email_dpf}')]]//div[contains(@class,'dropdown actions-dropdown')]"
        )

    @allure.step("Click refund button for payment from user '{email_dpf}' in Payments tab")
    def get_user_menu_refund_button_payments_tab(self, email_dpf):
        return self.page.locator(
            f"//tr[.//span[contains(text(),'{email_dpf}')]]//a[text()=' Refund']"
        )
