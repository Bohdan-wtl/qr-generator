import os
import allure
import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from config import download_params_default_modal


@allure.epic("QR Code Generation and Download")
@allure.feature(f"Default sign up flow - Browser: {os.getenv('BROWSER')}")
class TestDefaultSignUpFlowAll(BaseTest):
    @allure.title("Website QR Code Generation and Download Test")
    @allure.description(
        "Verify the complete flow of creating and downloading a website QR code with different formats and resolutions"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create"])
    def test_default_sign_up_website_qr_type(
        self, page, sign_up_fixture, qr_create_method, fake_email
    ):
        with allure.step("Initialize QR code creation for website"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Verify and click create button"):
            expect(self.qr_creation_page.locator.create_button).to_be_disabled()

            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()

        with allure.step("Verify successful QR code generation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)
            self.my_qr_codes_page.locator.download_modal_close_button.click()

        for params in download_params_default_modal:
            with allure.step(
                f"Download QR code - Format: {params['file_format']}, Resolution: {params['resolution']}px"
            ):
                self.page.wait_for_timeout(7000)
                with allure.step("Open download modal"):
                    self.my_qr_codes_page.locator.download_qr_code_button.click()
                with allure.step(
                    f"Select format {params['file_format']} and resolution {params['resolution']}px"
                ):
                    self.my_qr_codes_page.download_parametrize_files(
                        file_format=params["file_format"],
                        resolution=params["resolution"],
                    )
