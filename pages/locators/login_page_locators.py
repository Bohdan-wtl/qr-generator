class LoginPageLocators:

    def __init__(self, page):
        self.email_log_in = page.locator("//input[@id='input-email']")
        self.password_log_in = page.locator("//input[@id='input-password']")
        self.log_in_confirm_button = page.locator("//button[@id='login-btn']")
