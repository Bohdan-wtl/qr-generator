from turtle import delay
import allure

from base.base_page import BasePage
from pages.locators.payment_page_locators import PaymentPageLocators


class PaymentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = PaymentPageLocators(page)

    @allure.step("Process payment with test credit card")
    def make_payment(self):
        with allure.step("Enter card number: 4242 4242 4242 4242"):
            self.checked_locator(locator=self.locator.card_number_label)
            self.checked_locator(locator=self.locator.card_number).fill("4242 4242 4242 4242")
        with allure.step("Enter expiry date: 01/27"):
            self.checked_locator(locator=self.locator.expiry_date_input).fill("0127")
        with allure.step("Enter CVC code: 127"):
            self.checked_locator(locator=self.locator.cvc_code_input).fill("127")
        with allure.step("Exit payment frame"):
            self.checked_locator(locator=self.locator.exit_from_payment_frame).click()

    @allure.step("Submit payment transaction")
    def click_on_submit_payment_button(self):
        with allure.step("Wait for and click submit payment button"):
            self.locator.submit_payment_button.wait_for(state="visible", timeout=40000)
            self.checked_locator(locator=self.locator.submit_payment_button).click()

    @allure.step("Fill billing address details")
    def select_country_and_zip_in_payment_frame(self):
        with allure.step("Select country: United States"):
            self.checked_locator(locator=self.locator.payment_country_dropdown).select_option(value="US")
        with allure.step("Enter ZIP code: 90001"):
            self.checked_locator(locator=self.locator.payment_zip_input).fill("90001")
        with allure.step("Exit payment frame"):
            self.checked_locator(locator=self.locator.exit_from_payment_frame).click()
