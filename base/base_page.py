from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def open_page(self, url):
        self.page.goto(url)

    def checked_locator(self, locator):
        self.expect(locator).to_be_visible(timeout=40000)
        self.expect(locator).to_be_enabled(timeout=40000)
        return locator

    def is_visible(self, locator):
        self.expect(locator).to_be_visible()
        return locator

    def is_invisible(self, locator):
        self.expect(locator).not_to_be_visible()
        return True

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
