from datetime import datetime
import os

import allure

from base.base_page import BasePage
from pages.locators.my_qr_codes_locators import MyQrCodesLocators


class MyQrCodesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = MyQrCodesLocators(page)

    @allure.step("Download QR code to {download_path}")
    def file_download(self, download_path):
        with allure.step("Initiate QR code download"):
            with self.page.expect_download() as download_info:
                self.locator.download_button.click()
            download = download_info.value
        
        with allure.step("Save QR code with timestamped filename"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{timestamp}_{download.suggested_filename}"
            file_path = os.path.join(download_path, file_name)
            download.save_as(file_path)
            assert os.path.exists(file_path), "QR code not downloaded"

    @allure.step("Download QR code in {file_format} format with {resolution} resolution")
    def download_parametrize_files(self, file_format, resolution):
        download_path = "artifacts/downloaded_qr_path/"
        self.checked_locator(locator=self.page.locator(
            f"//div[contains(@class,'dl-modal-option-card')]//h6[text()='{file_format}']"
        )).click()
        self.locator.size_of_qr_file_download_dropdown.click(force=True)
        self.page.locator(f"//input[@id='{resolution}']").click()
        with self.page.expect_download() as download_info:
            self.checked_locator(self.locator.download_button).click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = (
            f"{file_format}_{resolution}_{timestamp}_{download.suggested_filename}"
        )
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"

    @allure.step("Open QR code link for code named: {qr_name}")
    def open_qr_link(self, qr_name):
        qr_link = self.page.locator(
            f"//span[text()='{qr_name}']/../../../..//a[@class='qr-card-link']"
        ).first
        return qr_link

    @allure.step("Open most recently created QR code link")
    def open_last_qr_link(self):
        qr_link = self.page.locator("//a[@class='qr-card-link']").first
        return qr_link

    @allure.step("Disable iframe preview on webview page")
    def turn_off_iframe(self):
        self.page.locator("body").press("ControlOrMeta+.")
