class MainPageLocators:

    def __init__(self, page):
        self.log_in_button = page.get_by_role("a.-link-log-in.non-draggable")
        self.sign_up_button = page.get_by_role("a.-link-sign-up.non-draggable")
        self.main_logo_link = page.locator(".billing-nav .animate-logo")
