import allure

from base.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = MainPageLocators(page)

    @allure.step("Navigate to login page from main menu")
    def go_to_log_in_page(self):
        with allure.step("Click login button in navigation"):
            self.checked_locator(locator=self.locator.log_in_button).click()

    @allure.step("Navigate to sign up page from main menu")
    def go_to_sign_up_page(self):
        with allure.step("Click sign up button in navigation"):
            self.checked_locator(locator=self.locator.sign_up_button).click()
