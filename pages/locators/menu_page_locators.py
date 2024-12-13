from base.base_page import BasePage


class MenuPageLocators:

    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        self.create_qr_code = self.base.locator("//ul[@class='app-sidebar-links']/li[1]")
        self.analytics = self.base.locator("//ul[@class='app-sidebar-links']/li[2]")
        self.my_qr_codes = self.base.locator("//ul[@class='app-sidebar-links']/li[3]")
        self.my_account = self.base.locator("//ul[@class='app-sidebar-links']/li[4]")
        self.billing = self.base.locator("//ul[@class='app-sidebar-links']/li[5]")
