class RegisterPageLocators:
    def __init__(self, page):
        self.email_input_field = page.locator("//input[@id='input-email']")
        self.password_input_field = page.locator("//input[@id='input-password']")
        self.sign_up_confirm_button = page.locator("//button[@type='submit']")