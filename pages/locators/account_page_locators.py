from base.base_page import BasePage


class AccountPageLocators:
    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        self.my_account_name = self.base.locator("//input[@id='name']")
        self.my_account_surname = self.base.locator("//input[@id='surname']")
        self.my_account_email = self.base.locator("//div[@class='input-field-area']/input[@id='email']")
        self.my_account_telephone = self.base.locator("//input[@id='telephone']")
        self.personal_info_submit_button = self.base.locator("//button[@id='sbmt']")
        self.password_update_input = self.base.locator("//input[@id='password']")
        self.password_update_confirm_input = self.base.locator("//input[@id='re_password']")
        self.password_update_submit_button = self.base.locator("//button[@id='passSave']")
        self.language_update = self.base.locator("//select[@id='language']")
        self.language_update_button = self.base.locator("//button[@id='LangSave']")
        self.log_out_button = self.base.locator("//span[@class='icon-sign-out']/parent::a")