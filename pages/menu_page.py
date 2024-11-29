import allure

from base.base_page import BasePage
from pages.locators.menu_page_locators import MenuPageLocators

class MenuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = MenuPageLocators(page)

    @allure.step("Go to my account")
    def go_to_my_account(self):
        self.locator.my_account.click()