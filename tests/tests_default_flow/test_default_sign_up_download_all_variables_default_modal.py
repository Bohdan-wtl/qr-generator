import os
import time
import allure
import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from config import languages, qr_create_methods, download_params_default_modal


@pytest.mark.parametrize("language", languages)
@allure.feature(f"Default sign up flow - {os.getenv('BROWSER')} - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlow(BaseTest):

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    def test_default_sign_up_qr_type(self, sign_up_fixture, qr_create_method, fake_email):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        expect(self.qr_creation_page.locator.create_button).to_be_disabled()
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        self.my_qr_codes_page.locator.download_modal_close_button.click()
        for params in download_params_default_modal:
            with allure.step(f"Download QR code as {params['file_format']} with resolution {params['resolution']}"):
                time.sleep(2)
                self.my_qr_codes_page.locator.download_qr_code_button.click()
                self.my_qr_codes_page.locator.svg_file_download.wait_for(state="visible", timeout=10000)

                self.my_qr_codes_page.download_parametrize_files(
                    file_format=params["file_format"],
                    resolution=params["resolution"]
            )


    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create", "menu_link_qr_create"])
    def test_default_sign_up_website_qr_type(self, sign_up_fixture, qr_create_method, fake_email):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        expect(self.qr_creation_page.locator.create_button).to_be_disabled()
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        self.my_qr_codes_page.locator.download_modal_close_button.click()

        for params in download_params_default_modal:
            with allure.step(f"Download QR code as {params['file_format']} with resolution {params['resolution']}"):
                self.my_qr_codes_page.locator.download_qr_code_button.click()
                self.my_qr_codes_page.download_parametrize_files(
                    file_format=params["file_format"],
                    resolution=params["resolution"]
            )
