import os

import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import eps_download_format, qr_create_methods, resolution_qr_code_images


@allure.feature(f"CFF Flow - EPS Format - {os.getenv('BROWSER')}")
@allure.story("QR Code Creation and Download Flow")
class TestCFFSignUpFlowEps(BaseTest):
    @allure.title("Test CFF sign up with different QR creation methods")
    @allure.description(f"Verify QR code {qr_create_methods} creation and EPS download functionality with various methods and resolutions {resolution_qr_code_images}")
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_cff_sign_up_qr_type(
        self, navigate_to_dpf_page, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Navigate to DPF page and verify current URL"):
            print("Current url - " + self.qr_creation_page.get_url())
        
        with allure.step(f"Create QR code using method: {qr_create_method}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()
        
        with allure.step("Complete QR code creation steps"):
            self.qr_creation_page.click_next_button_step2()
            self.qr_creation_page.complete_step_3()
            
        with allure.step("Verify and handle create button state"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
            except AssertionError:
                allure.attach("Button State", "The button has not become disabled, continuing the test")
        
        with allure.step("Submit form with email"):
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()
            self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
            self.qr_creation_page.locator.dpf_form_submit_button.click()
        
        with allure.step("Verify successful signup"):
            self.main_page.locator.main_logo_link.click()
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)
        
        with allure.step(f"Download QR code in EPS format with resolution {resolution}"):
            self.my_qr_codes_page.download_parametrize_files(eps_download_format, resolution)

    @allure.title("Test CFF sign up with website QR creation")
    @allure.description("Verify website QR code creation and EPS download functionality")
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create", "menu_link_qr_create"])
    @pytest.mark.parametrize("resolution", resolution_qr_code_images)
    def test_cff_sign_up_website_qr_type(
        self, navigate_to_dpf_page, qr_create_method, fake_email, resolution
    ):
        with allure.step(f"Create website QR code using method: {qr_create_method}"):
            qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
            qr_create_method_func()
        
        with allure.step("Verify and handle create button state"):
            try:
                expect(self.qr_creation_page.locator.create_button).to_be_disabled(timeout=5000)
            except AssertionError:
                allure.attach("Button State", "The button has not become disabled, continuing the test")
        
        with allure.step("Complete signup process"):
            self.qr_creation_page.locator.create_button.is_enabled()
            self.qr_creation_page.locator.create_button.click()
            self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
            self.qr_creation_page.locator.dpf_form_submit_button.click()
        
        with allure.step("Verify successful signup"):
            self.main_page.locator.main_logo_link.click()
            self.my_qr_codes_page.expect(
                self.my_qr_codes_page.locator.sign_up_success_image
            ).to_be_enabled(timeout=30000)
        
        with allure.step(f"Download QR code in EPS format with resolution {resolution}"):
            self.my_qr_codes_page.download_parametrize_files(eps_download_format, resolution)
