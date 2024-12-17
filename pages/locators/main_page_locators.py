class MainPageLocators:

    def __init__(self, page):
        self.log_in_button = page.locator("//a[contains(@class, 'log-in')]")
        self.sign_up_button = page.locator("//a[contains(@class, 'sign-up')]")
        self.main_logo_link = page.locator(".billing-nav .animate-logo")
