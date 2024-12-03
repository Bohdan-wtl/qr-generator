import os
import allure
import pytest
from playwright.sync_api import expect

from base.base_test import BaseTest
from config import languages, qr_create_methods


@pytest.mark.parametrize("language", languages)
@allure.feature(f"Default sign up flow - {os.getenv('BROWSER')} - {os.getenv('BROWSER')}")
class TestDefaultSignUpFlow(BaseTest):

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    #@pytest.mark.parametrize("resolution", ["Default", "512x512", "1024x1024", "2048x2048", "4096x4096"])
    def test_default_sign_up_qr_type(self, sign_up_fixture, qr_create_method, fake_email):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        expect(self.qr_creation_page.locator.create_button).to_be_disabled()
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.download_parametrize_files("JPEG", resolution, "artifacts/download_qr_path_jpeg/")



    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create", "menu_link_qr_create"])
    #@pytest.mark.parametrize("resolution", ["Default", "512x512", "1024x1024", "2048x2048", "4096x4096"])
    def test_default_sign_up_website_qr_type(self, sign_up_fixture, qr_create_method, fake_email):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        expect(self.qr_creation_page.locator.create_button).to_be_disabled()
        self.qr_creation_page.locator.create_button.is_enabled()
        self.qr_creation_page.locator.create_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.download_parametrize_files("JPEG", resolution, "artifacts/download_qr_path_jpeg/")
