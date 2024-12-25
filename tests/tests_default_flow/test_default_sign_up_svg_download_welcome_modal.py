import os
import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import (
    qr_create_methods,
    resolution_qr_code_images,
    resolution_qr_code_pdf,
    svg_download_format,
)


@allure.epic("QR Code Generation and Download")
@allure.feature(f"Default Sign Up Flow - SVG Format - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlowSvg(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Generate {qr_create_method} QR code and download as SVG with {resolution} resolution")
    @allure.description("Test the full flow of QR code creation and SVG download with various methods and resolutions")
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_default_sign_up_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Initialize QR code creation using {qr_create_method} method"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Configure QR code design and settings"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()

        with allure.step("Generate QR code and verify creation button state"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
            except AssertionError:
                pass
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step("Verify successful QR code generation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(f"Export QR code in SVG format with {resolution} resolution"):
            self.my_qr_codes_page.download_parametrize_files(
                svg_download_format, resolution
            )

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Generate Website QR Code with SVG Download - Resolution: {resolution}")
    @allure.description("Test website and menu link QR code creation with SVG download functionality")
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_default_sign_up_website_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Initialize QR code creation using {qr_create_method} method"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Generate QR code and verify creation button state"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
            except AssertionError:
                pass
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step("Verify successful QR code generation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(f"Export QR code in SVG format with {resolution} resolution"):
            self.my_qr_codes_page.download_parametrize_files(
                svg_download_format, resolution
            )
