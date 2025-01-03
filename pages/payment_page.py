import allure

from base.base_page import BasePage
from pages.locators.payment_page_locators import PaymentPageLocators


class PaymentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = PaymentPageLocators(page)

    @allure.step("Process payment with test credit card")
    def make_payment(self):
        slow_mo = 1000
        with allure.step("Enter card number: 4242 4242 4242 4242"):
            self.checked_locator(locator=self.locator.card_number).clear()
            self.checked_locator(locator=self.locator.card_number).fill(
                "4242 4242 4242 4242", timeout=slow_mo
            )
        with allure.step("Enter expiry date: 01/27"):
            self.checked_locator(locator=self.locator.expiry_date_input).clear()
            self.checked_locator(locator=self.locator.expiry_date_input).fill(
                "0127", timeout=slow_mo
            )
        with allure.step("Enter CVC code: 127"):
            self.checked_locator(locator=self.locator.cvc_code_input).clear()
            self.checked_locator(locator=self.locator.cvc_code_input).fill(
                "127", timeout=slow_mo
            )
        with allure.step("Exit payment frame"):
            self.checked_locator(locator=self.locator.exit_from_payment_frame).click()

    @allure.step("Submit payment transaction")
    def click_on_submit_payment_button(self):
        with allure.step("Submit payment"):
            if (
                self.is_invisible(self.locator.card_number_error_label)
                and self.is_invisible(self.locator.exp_date_error_label)
                and self.is_invisible(self.locator.cvc_code_error_label)
            ):
                self.checked_locator(locator=self.locator.submit_payment_button).click()
            else:
                self.make_payment()

    @allure.step("Fill billing address details")
    def select_country_and_zip_in_payment_frame(self):
        with allure.step("Select country: United States"):
            self.checked_locator(
                locator=self.locator.payment_country_dropdown
            ).select_option(value="US")
        with allure.step("Enter ZIP code: 90001"):
            self.checked_locator(locator=self.locator.payment_zip_input).fill("90001")
        with allure.step("Exit payment frame"):
            self.checked_locator(locator=self.locator.exit_from_payment_frame).click()
