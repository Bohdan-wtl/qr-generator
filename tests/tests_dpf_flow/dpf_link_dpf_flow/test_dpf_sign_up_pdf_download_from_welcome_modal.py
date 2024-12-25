import os

import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import pdf_download_format, qr_create_methods, resolution_qr_code_pdf


@allure.feature(f"DPF Flow - PDF Format - {os.getenv('BROWSER')}")
class TestDPFSignUpFlowPdf(BaseTest):
    @allure.story("QR Code Creation with PDF Download")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Create QR code, complete DPF signup, and download PDF format")
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @pytest.mark.parametrize("resolution", resolution_qr_code_pdf)
    def test_dpf_sign_up_qr_type(
        self, navigate_to_dpf_page, qr_create_method, fake_email, resolution
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

        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.create_button
        ).click()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.dpf_form_submit_button
        ).click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.congrats_download_button
        ).click()
        self.my_qr_codes_page.expect(
            self.my_qr_codes_page.locator.sign_up_success_image
        ).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.download_parametrize_files(
            pdf_download_format, resolution
        )

    @allure.story("Website QR Creation with PDF Download")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Create website QR code, complete DPF signup, and download PDF format"
    )
    @pytest.mark.parametrize(
        "qr_create_method", ["website_qr_create", "menu_link_qr_create"]
    )
    @pytest.mark.parametrize("resolution", resolution_qr_code_pdf)
    def test_dpf_sign_up_website_qr_type(
        self, navigate_to_dpf_page, qr_create_method, fake_email, resolution
    ):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
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
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.checked_locator(
            self.qr_creation_page.locator.congrats_download_button
        ).click()
        self.my_qr_codes_page.expect(
            self.my_qr_codes_page.locator.sign_up_success_image
        ).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.download_parametrize_files(
            pdf_download_format, resolution
        )
