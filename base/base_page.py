from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def open_page(self, url):
        self.page.goto(url)

    def locator(self, selector: str, visible=True, enabled=True):
        locator = self.page.locator(selector)
        if visible:
            self.expect(locator).to_be_visible()
        if enabled:
            self.expect(locator).to_be_enabled()
        return locator

    def is_visible(self, locator):
        self.expect(self.page.locator(locator)).to_be_visible()

    def is_invisible(self, locator):
        self.expect(self.page.locator(locator)).to_be_hidden()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def open_in_new_tab(self, locator):
        with self.page.expect_popup() as popup_info:
            locator.click(button="left")
        new_page = popup_info.value
        return new_page

    def get_url(self):
        return self.page.url

    def title(self):
        return self.page.title()