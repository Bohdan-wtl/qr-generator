from base.base_page import BasePage
from pages.locators.plans_and_price_page_locators import PlansAndPriceLocators

class PlanAndPricesPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = PlansAndPriceLocators(page)