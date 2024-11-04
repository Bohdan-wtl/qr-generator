from random import Random
import pytest
from faker import Faker
from base.base_test import BaseTest
from config import languages_dpf_urls

@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
@pytest.mark.parametrize("dpf_language", languages_dpf_urls.keys())
class TestCFFSignUpFlow(BaseTest):
    
    @pytest.fixture(autouse=True)
    def setup_faker(self):
        self.faker = Faker()
        self.random_number = Random().randint(1000, 3000)
        self.fake_email = "wtl-automation" + str(self.random_number) + "@test.com"

    @pytest.fixture(scope='function')
    def navigate_to_dpf_page(self, dpf_language):
        stage_url = languages_dpf_urls[dpf_language]
        self.main_page.open_page(stage_url)

    def test_cff_sign_up_website_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.website_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_pdf_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.pdf_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_links_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.links_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_vcard_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.vcard_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_business_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.business_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_image_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.image_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_video_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.video_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_apps_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.apps_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_coupon_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.coupon_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_mp3_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.mp3_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_menu_menu_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.menu_menu_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_menu_pdf_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.menu_pdf_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_menu_link_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.menu_link_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_wifi_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.wifi_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_facebook_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.facebook_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_instagram_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.instagram_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_social_media_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.social_media_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_cff_sign_up_whats_app_qr_type(self, navigate_to_dpf_page):
        self.qr_creation_page.whatsapp_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(self.fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.main_page.main_logo_link.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
