from base.base_page import BasePage


class MainPageLocators:

    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        self.log_in_button = self.base.locator("//a[contains(@class, 'log-in')]")
        self.sign_up_button = self.base.locator("//a[contains(@class, 'sign-up')]")
        self.main_logo_link = self.base.locator(".billing-nav .animate-logo")
