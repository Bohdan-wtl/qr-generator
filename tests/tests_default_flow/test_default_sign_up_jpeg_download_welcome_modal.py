import os
import allure
import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from config import jpeg_download_format, qr_create_methods, resolution_qr_code_images


@allure.epic("QR Code Generation and Download")
@allure.feature(f"Default Sign Up Flow - JPEG Format - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlowJpeg(BaseTest):

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("JPEG QR Code Generation")
    @allure.title("Create {qr_create_method} QR Code with JPEG Download ({resolution})")
    @allure.description(
        """
        Full testing cycle for QR code generation with JPEG download:
        - QR code creation using specified method
        - Configuration and customization
        - Generation verification
        - JPEG format export
    """
    )
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_default_sign_up_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(
            f"Begin {qr_create_method.replace('_', ' ')} QR code creation workflow"
        ):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Customize QR code design and parameters"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()

        with allure.step("Complete QR code generation process"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                self.qr_creation_page.checked_locator(
                    self.qr_creation_page.locator.congrats_download_button
                ).click()("Button State", "The button has not become disabled")

            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()

        with allure.step(f"Save QR code as JPEG image with {resolution} quality"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(
            f"Download QR code with {resolution} resolution in JPEG format"
        ):
            self.my_qr_codes_page.download_parametrize_files(
                jpeg_download_format, resolution
            )

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Website QR Code Creation")
    @allure.description(
        "Test the creation of website and menu link QR codes with JPEG download"
    )
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_default_sign_up_website_qr_type(
        self, sign_up_fixture, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Create {qr_create_method.replace('_', ' ')}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()

        with allure.step("Verify and click create button"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                    timeout=5000
                )
            except AssertionError:
                allure.attach("Button State", "The button has not become disabled")

            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()

        with allure.step("Verify successful QR code generation"):
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)

        with allure.step(
            f"Download QR code with {resolution} resolution in JPEG format"
        ):
            self.my_qr_codes_page.download_parametrize_files(
                jpeg_download_format, resolution
            )
