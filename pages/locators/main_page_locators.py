class MainPageLocators:

    def __init__(self, page):
        self.log_in_button = page.locator("//div[@class='-login-signup']/a[@class='-link-log-in non-draggable']")
        self.sign_up_button = page.locator("//div[@class='-login-signup']/a[@class='-link-sign-up non-draggable']")
        self.main_logo_link = page.locator("//nav[@class='billing-nav']/a")
