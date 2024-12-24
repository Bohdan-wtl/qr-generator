import os
import allure
import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from config import download_params_default_modal


@allure.feature(f"Default sign up flow - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlowAll(BaseTest):
    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create"])
    def test_default_sign_up_website_qr_type(
        self, page, sign_up_fixture, qr_create_method, fake_email
    ):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        expect(self.qr_creation_page.locator.create_button).to_be_disabled()
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.my_qr_codes_page.expect(
            self.my_qr_codes_page.locator.sign_up_success_image
        ).to_be_enabled(timeout=30000)
        self.my_qr_codes_page.locator.download_modal_close_button.click()

        for params in download_params_default_modal:
            with allure.step(
                f"Download QR code as {params['file_format']} with resolution {params['resolution']}"
            ):
                self.page.wait_for_timeout(7000)
                self.my_qr_codes_page.locator.download_qr_code_button.click()
                self.my_qr_codes_page.download_parametrize_files(
                    file_format=params["file_format"], resolution=params["resolution"]
                )
