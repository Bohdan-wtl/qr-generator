import allure
import pytest
from base.base_test import BaseTest
from config import languages_dpf_urls


@pytest.mark.parametrize("dpf_language", languages_dpf_urls.keys())
@allure.feature("CFF sign up flow")
@pytest.mark.parametrize("browser", ["chromium", "webkit"], indirect=True)
class TestCFFSignUpFlow(BaseTest):

    @allure.title("Website QR type")
    def test_cff_sign_up_website_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.website_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("PDF QR type")
    def test_cff_sign_up_pdf_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()


    @allure.title("Links QR type")
    def test_cff_sign_up_links_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.links_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled(timeout=3000)

    @allure.title("VCard QR type")
    def test_cff_sign_up_vcard_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.vcard_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Business QR type")
    def test_cff_sign_up_business_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.business_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled(timeout=30000)

    @allure.title("Image QR type")
    def test_cff_sign_up_image_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.image_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Video QR type")
    def test_cff_sign_up_video_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.video_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Apps QR type")
    def test_cff_sign_up_apps_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.apps_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Coupon QR type")
    def test_cff_sign_up_coupon_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.coupon_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("MP3 QR type")
    def test_cff_sign_up_mp3_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.mp3_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Menu-Menu QR type")
    def test_cff_sign_up_menu_menu_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.menu_menu_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Menu-PDF QR type")
    def test_cff_sign_up_menu_pdf_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.menu_pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Menu-Link QR type")
    def test_cff_sign_up_menu_link_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.menu_link_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("WiFi QR type")
    def test_cff_sign_up_wifi_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.wifi_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Facebook QR type")
    def test_cff_sign_up_facebook_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.facebook_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Instagram QR type")
    def test_cff_sign_up_instagram_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.instagram_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("Social_media QR type")
    def test_cff_sign_up_social_media_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.social_media_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @allure.title("WhatsApp QR type")
    def test_cff_sign_up_whats_app_qr_type(self, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.whatsapp_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.locator.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
