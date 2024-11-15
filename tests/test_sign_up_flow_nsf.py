import os
import allure
import pytest
from base.base_test import BaseTest
from config import languages_nsf_urls


@pytest.mark.parametrize(f"nsf_language", languages_nsf_urls.keys())
@allure.feature(f"NSF sign up flow - {os.getenv('BROWSER')}")
class TestNSFSignUpFlow(BaseTest):

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["wifi_qr_create", "instagram_qr_create",
                                                  "mp3_qr_create", "coupon_qr_create",
                                                  "menu_menu_qr_create", "facebook_qr_create", "apps_qr_create",
                                                  "links_qr_create", "menu_pdf_qr_create", "pdf_qr_create",
                                                  "social_media_qr_create", "whatsapp_qr_create", "video_qr_create",
                                                  "image_qr_create", "business_qr_create", "vcard_qr_create",
                                                  ])
    def test_dpf_sign_up_qr_type(self, navigate_to_nsf_page, qr_create_method, fake_email):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["website_qr_create", "menu_link_qr_create"])
    def test_dpf_sign_up_website_qr_type(self, navigate_to_nsf_page, qr_create_method, fake_email):
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
