import allure

from base.base_page import BasePage
from pages.locators.payment_page_locators import PaymentPageLocators

class PaymentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = PaymentPageLocators(page)

    @allure.step("Make payment")
    def make_payment(self):
        self.checked_locator(locator=self.locator.card_number).fill("4242424242424242")
        self.checked_locator(locator=self.locator.expiry_date_input).fill("0127")
        self.checked_locator(locator=self.locator.cvc_code_input).fill("127")
        self.checked_locator(locator=self.locator.exit_from_payment_frame).click()

    @allure.step("Click on submit payment button")
    def click_on_submit_payment_button(self):
        self.locator.submit_payment_button.wait_for(state='visible', timeout=40000)
        self.checked_locator(locator=self.locator.submit_payment_button).click()

    @allure.step("Select country and zip in payment frame")
    def select_country_and_zip_in_payment_frame(self):
        self.checked_locator(locator=self.locator.payment_country_dropdown).select_option(value="US")
        self.checked_locator(locator=self.locator.payment_zip_input).fill("90001")
        self.checked_locator(locator=self.locator.exit_from_payment_frame).click()