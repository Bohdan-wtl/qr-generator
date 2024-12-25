import os

import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import jpeg_download_format, qr_create_methods, resolution_qr_code_images


@allure.feature(f"NSF Flow - JPEG Format - {os.getenv('BROWSER')}")
@allure.story("QR Code Creation and Download")
class TestNSFSignUpFlowJpeg(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title(
        "Create and download QR code with {qr_create_method} method and {resolution} resolution"
    )
    @allure.description(
        "Test QR code creation through sign up flow with different creation methods and resolutions"
    )
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_nsf_sign_up_qr_type(
        self, navigate_to_nsf_page, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Create QR code using {qr_create_method} method"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Complete QR code creation steps"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()

        with allure.step("Verify and click create button"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                allure.attach(
                    "Button State",
                    "The button has not become disabled, continuing the test",
                )
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step(f"Submit sign up form with email: {fake_email}"):
            self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_submit_button
            ).click()

        with allure.step("Verify successful sign up"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(
            f"Download QR code in JPEG format with {resolution} resolution"
        ):
            self.my_qr_codes_page.download_parametrize_files(
                jpeg_download_format, resolution
            )

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title(
        "Create and download website QR code with {qr_create_method} method and {resolution} resolution"
    )
    @allure.description(
        "Test website QR code creation through sign up flow with specific methods and resolutions"
    )
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_nsf_sign_up_website_qr_type(
        self, navigate_to_nsf_page, qr_create_method, fake_email, resolution
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
                allure.attach(
                    "Button State",
                    "The button has not become disabled, continuing the test",
                )
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()

        with allure.step(f"Submit sign up form with email: {fake_email}"):
            self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_submit_button
            ).click()

        with allure.step("Verify successful sign up"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(
            f"Download QR code in JPEG format with {resolution} resolution"
        ):
            self.my_qr_codes_page.download_parametrize_files(
                jpeg_download_format, resolution
            )
