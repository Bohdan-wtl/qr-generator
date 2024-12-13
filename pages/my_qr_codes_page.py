from datetime import datetime
import os

import allure
import pytest

from base.base_page import BasePage
from pages.locators.my_qr_codes_locators import MyQrCodesLocators


class MyQrCodesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = MyQrCodesLocators(page)

    @allure.step("Download QR code")
    def file_download(self, download_path):
        with self.page.expect_download() as download_info:
            self.locator.download_button.click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{timestamp}_{download.suggested_filename}"
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"

    @allure.step("Download QR code with parameters")
    def download_parametrize_files(self, file_format, resolution):
        download_path = "artifacts/downloaded_qr_path/"
        format_selector = f"//div[contains(@class,'dl-modal-option-card')]//h6[text()='{file_format}']"
        self.page.locator(format_selector).click()
        self.checked_locator(locator=self.locator.size_of_qr_file_download_dropdown).click(force=True)
        resolution_selector = f"//input[@id='{resolution}']"
        self.page.locator(resolution_selector).click()
        with self.page.expect_download() as download_info:
            self.checked_locator(locator=self.locator.download_button).click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{file_format}_{resolution}_{timestamp}_{download.suggested_filename}"
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"

    @allure.step("Open QR code link")
    def open_qr_link(self, qr_name):
        qr_link = self.page.locator(f"//span[text()='{qr_name}']/../../../..//a[@class='qr-card-link']").first
        return qr_link

    @allure.step("Open last QR code link")
    def open_last_qr_link(self):
        qr_link = self.page.locator("//a[@class='qr-card-link']").first
        return qr_link

    @allure.step("Turn off iframe on webview page")
    def turn_off_iframe(self):
        self.page.locator("body").press("ControlOrMeta+.")
