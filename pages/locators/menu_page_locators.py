class MenuPageLocators:

    def __init__(self, page):
        self.create_qr_code = page.locator("//ul[@class='app-sidebar-links']/li[1]")
        self.analytics = page.locator("//ul[@class='app-sidebar-links']/li[2]")
        self.my_qr_codes = page.locator("//ul[@class='app-sidebar-links']/li[3]")
        self.my_account = page.locator("//ul[@class='app-sidebar-links']/li[4]")
        self.billing = page.locator("//ul[@class='app-sidebar-links']/li[5]")
