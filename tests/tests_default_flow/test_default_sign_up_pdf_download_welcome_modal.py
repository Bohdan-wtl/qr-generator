import os

import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import pdf_download_format, qr_create_methods, resolution_qr_code_pdf

@allure.epic("QR Code Generation and Download")
@allure.feature(f"Default Sign Up Flow - PDF Format - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlowPdf(BaseTest):
    @allure.story("PDF QR Code Generation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Generate {qr_create_method} QR Code - PDF Format ({resolution})")
    @allure.description("""
        Comprehensive test of QR code generation workflow:
        1. Create QR code using specified method
        2. Configure settings and design
        3. Generate and verify
        4. Download in PDF format
    """)
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_pdf)
    def test_default_sign_up_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Initialize new {qr_create_method.replace('_', ' ')} QR code creation"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Configure QR code appearance and settings"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()

        with allure.step("Generate QR code and verify process completion"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
            except AssertionError:
                allure.attach("Button State", "The button has not become disabled, continuing the test")
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step(f"Export QR code as PDF document with {resolution} quality"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)
            self.my_qr_codes_page.download_parametrize_files(
                pdf_download_format, resolution
            )

    @allure.story("Website QR Code Creation")
    @allure.description("Test creating website and menu link QR codes with PDF download")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_pdf)
    def test_default_sign_up_website_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Creating {qr_create_method.replace('_', ' ')}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Verifying and clicking create button"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
            except AssertionError:
                self.qr_creation_page.locator.create_button.is_enabled()
                self.qr_creation_page.locator.create_button.click()

        with allure.step("Verifying successful QR code creation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(f"Downloading QR code PDF with resolution: {resolution}"):
            self.my_qr_codes_page.download_parametrize_files(
                pdf_download_format, resolution
            )
