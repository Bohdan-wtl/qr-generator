import os

import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import png_download_format, qr_create_methods, resolution_qr_code_images


@allure.epic("QR Code Generation")
@allure.feature(f"CFF Flow - PNG Format - {os.getenv('BROWSER')}")
class TestCFFSignUpFlowPng(BaseTest):
    @allure.story("QR Code Creation and Download")
    @allure.title(
        "Create and download QR code with different creation methods and resolutions"
    )
    @allure.description(
        "Test creates QR code using different methods, completes signup flow and downloads PNG file"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_cff_sign_up_qr_type(
        self, navigate_to_dpf_page, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Creating QR code using method: {qr_create_method}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Completing QR code creation steps"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                "The button has not become disabled, continuing the test"

            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()
            self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_submit_button
            ).click()
            self.main_page.locator.main_logo_link.click()
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)
            self.my_qr_codes_page.download_parametrize_files(
                png_download_format, resolution
            )

    @allure.story("Website QR Code Creation")
    @allure.title("Create and download website QR code with different resolutions")
    @allure.description(
        "Test creates website/menu QR code, completes signup flow and downloads PNG file"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_cff_sign_up_website_qr_type(
        self, navigate_to_dpf_page, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Creating website QR code using method: {qr_create_method}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Completing signup flow"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                allure.attach(
                    "Button state",
                    "The button has not become disabled, continuing the test",
                )

            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()
            self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_submit_button
            ).click()
            self.main_page.locator.main_logo_link.click()
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)
            self.my_qr_codes_page.download_parametrize_files(
                png_download_format, resolution
            )
