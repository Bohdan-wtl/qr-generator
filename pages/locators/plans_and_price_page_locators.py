class PlansAndPriceLocators:

    def __init__(self, page):
        self.variable_plan_button_universal_locator = page.locator(
            "//div[@class='buy-btn-area']//a[@data-plan-name='Monthly'] | //div[@class='buy-btn-area']//a[@data-plan-name='Annually'] | //div[@class='buy-btn-area']//a[@data-plan-name='Quarterly'] | //div[@class='buy-btn-area']//a[@data-plan-name='One Time'] | //div[@class='buy-btn-area']//a[@data-plan-name='Discounted']")
        # self.variable_plan_button_universal_locator = page.locator("//div[@class='trigger']")
        self.monthly_buy_now_button = page.locator("//a[@data-plan-name='Monthly']")
        self.annually_buy_now_button = page.locator("//a[@data-plan-name='Annually']")
        self.quarterly_buy_now_button = page.locator("//a[@data-plan-name='Quarterly']")
        self.continue_button = page.locator("#user_plan_url")

