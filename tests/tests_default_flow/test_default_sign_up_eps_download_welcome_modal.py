import os
import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import qr_create_methods, resolution_qr_code_images, eps_download_format

@allure.epic("QR Code Generation")
@allure.feature(f"Default Sign Up Flow - EPS Format - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlowEps(BaseTest):
    @allure.story("QR Code Creation with EPS Download")
    @allure.title("Create and download QR code with {qr_create_method} method at {resolution} resolution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_default_sign_up_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Create QR code using {qr_create_method} method"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Complete QR code configuration steps"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()

        with allure.step("Verify and click create button"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                allure.attach("Button state", "The button has not become disabled, continuing the test")
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step("Verify successful QR code creation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(f"Download QR code in EPS format at {resolution} resolution"):
            self.my_qr_codes_page.download_parametrize_files(
                eps_download_format, resolution
            )

    @allure.story("Website QR Code Creation with EPS Download")
    @allure.title("Create and download website QR code using {qr_create_method} at {resolution} resolution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_default_sign_up_website_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Create website QR code using {qr_create_method}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Verify and click create button"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                allure.attach("Button state", "The button has not become disabled, continuing the test")
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step("Verify successful QR code creation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(f"Download QR code in EPS format at {resolution} resolution"):
            self.my_qr_codes_page.download_parametrize_files(
                eps_download_format, resolution
            )
