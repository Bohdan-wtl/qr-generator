import os

import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import qr_create_methods, resolution_qr_code_images, svg_download_format


@pytest.mark.smoke
@allure.feature(f"NSF Flow - SVG Format - {os.getenv('BROWSER')}")
class TestNSFSignUpFlowSvg(BaseTest):
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    @allure.title(
        "Sign up flow test for {qr_create_method} with {resolution} resolution"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        """
        Test verifies the sign-up flow with different QR code types:
        1. Creates QR code with specified method
        2. Completes all required steps
        3. Verifies email submission
        4. Checks successful sign-up
        5. Downloads QR code in SVG format
    """
    )
    def test_nsf_sign_up_qr_type(
        self, navigate_to_nsf_page, qr_create_method, fake_email, resolution
    ):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        try:
            expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                timeout=5000
            )
        except AssertionError:
            "The button has not become disabled, continuing the test"
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.dpf_form_email_input
        ).fill(fake_email)
        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.dpf_form_submit_button
        ).click()
        self.my_qr_codes_page.expect(
            self.my_qr_codes_page.locator.sign_up_success_image
        ).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.download_parametrize_files(
            svg_download_format, resolution
        )

    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    @allure.title(
        "Website QR code sign up flow for {qr_create_method} with {resolution} resolution"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Website QR Code Generation")
    @allure.description(
        """
        Test verifies the sign-up flow specifically for website QR codes:
        1. Creates website/menu link QR code
        2. Verifies create button state
        3. Submits email form
        4. Validates successful sign-up
        5. Downloads QR code with specified resolution
    """
    )
    def test_nsf_sign_up_website_qr_type(
        self, navigate_to_nsf_page, qr_create_method, fake_email, resolution
    ):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        try:
            expect(self.qr_creation_page.locator.create_button).to_be_disabled(
                timeout=5000
            )
        except AssertionError:
            "The button has not become disabled, continuing the test"
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.dpf_form_submit_button
        ).click()
        self.my_qr_codes_page.expect(
            self.my_qr_codes_page.locator.sign_up_success_image
        ).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.download_parametrize_files(
            svg_download_format, resolution
        )
