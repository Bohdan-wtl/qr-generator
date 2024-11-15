import os

import allure
import pytest
from base.base_test import BaseTest
from config import languages_urls



@allure.feature(f"CFF sign up flow - {os.getenv('BROWSER')}")
@pytest.mark.parametrize("language", languages_urls.keys())
@pytest.mark.skip(reason="Debugging test")
class TestDebug(BaseTest):

    @allure.title(f"Website QR type -  {os.getenv('BROWSER')}")
    def test_website_qr_code_create(self, sign_up_fixture, fake_email):
        self.qr_creation_page.website_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title(f"PDF QR type - {os.getenv('BROWSER')}")
    def test_pdf_qr_code_create(self, sign_up_fixture, fake_email):
        self.qr_creation_page.pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()