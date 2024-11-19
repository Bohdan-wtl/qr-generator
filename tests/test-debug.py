import os
import allure
import pytest
from base.base_test import BaseTest
from config import languages_urls



@allure.feature(f"CFF sign up flow - {os.getenv('BROWSER')}")
@pytest.mark.parametrize("language", languages_urls.keys())
@pytest.mark.skip(reason="Fix is not ready yet")
class TestDebug(BaseTest):

    @allure.title(f"Website QR type -  {os.getenv('BROWSER')}")
    def test_website_qr_code_create(self, sign_up_fixture, fake_email):
        self.qr_creation_page.website_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()