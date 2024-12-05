import os
import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import languages, qr_create_methods, resolution_qr_code_images, svg_download_format


@pytest.mark.parametrize("language", languages)
@allure.feature(f"NSF sign up flow - {os.getenv('BROWSER')}")
class TestNSFSignUpFlow(BaseTest):

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_dpf_sign_up_qr_type(self, navigate_to_nsf_page, qr_create_method, fake_email, resolution):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        try:
            expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
        except AssertionError: "The button has not become disabled, continuing the test"
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.download_parametrize_files(svg_download_format, resolution)

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create", "menu_link_qr_create"])
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_dpf_sign_up_website_qr_type(self, navigate_to_nsf_page, qr_create_method, fake_email, resolution):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        try:
            expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
        except AssertionError: "The button has not become disabled, continuing the test"
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.download_parametrize_files(svg_download_format, resolution)
