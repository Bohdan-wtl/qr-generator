class MainPageLocators:

    def __init__(self, page):
        self.log_in_button = page.get_by_role("link", name=" Log In")
        self.sign_up_button = page.get_by_role("link", name=" Sign Up")
        self.main_logo_link = page.locator(".billing-nav .animate-logo")
