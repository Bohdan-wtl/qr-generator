from datetime import datetime
import os
from base.base_page import BasePage
from pages.locators.my_qr_codes_locators import MyQrCodesLocators


class MyQrCodesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = MyQrCodesLocators(page)

    def file_download(self, download_path):
        with self.page.expect_download() as download_info:
            self.locator.download_button.click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{timestamp}_{download.suggested_filename}"
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"

    def download_parametrize_files(self, file_format, resolution, download_path):
        format_selector = f"//div[contains(@class,'dl-modal-option-card')]//h6[text()='{file_format}']"
        self.page.locator(format_selector).click()
        self.locator.size_of_qr_file_download_dropdown.click(force=True)
        resolution_selector = f"//input[@id='{resolution}']"
        self.page.locator(resolution_selector).click()
        with self.page.expect_download() as download_info:
            self.locator.download_button.click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{file_format}_{resolution}_{timestamp}_{download.suggested_filename}"
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"