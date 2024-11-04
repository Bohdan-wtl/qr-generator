from base.base_page import BasePage
from pages.locators.payment_page_locators import PaymentPageLocators

class PaymentPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = PaymentPageLocators(page)

    def make_payment(self):
        self.locator.card_number.fill("4242424242424242")
        self.locator.expiry_date_input.fill("0127")
        self.locator.cvc_code_input.fill("127")
        self.locator.exit_from_payment_frame.click()

    def click_on_submit_payment_button(self):
        self.locator.submit_payment_button.wait_for(state='visible', timeout=40000)
        self.locator.submit_payment_button.click()