import pytest
from base.base_test import BaseTest
from config import languages_urls


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestDefaultSignUpFlow(BaseTest):
    
    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_website_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.website_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_pdf_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_links_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.links_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_vcard_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.vcard_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_business_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.business_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_images_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.image_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_video_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.video_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_apps_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.apps_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_coupon_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.coupon_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_mp3_qr_code_create(self, sign_up_fixture, language):
        self.qr_creation_page.mp3_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_menu_qr_code_create_menu_type(self, sign_up_fixture, language):
        self.qr_creation_page.menu_menu_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_menu_qr_code_create_pdf_type(self, sign_up_fixture, language):
        self.qr_creation_page.menu_pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_menu_qr_code_create_link_type(self, sign_up_fixture, language):
        self.qr_creation_page.menu_link_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_wi_fi_qr_code_type(self, sign_up_fixture, language):
        self.qr_creation_page.wifi_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_facebook_qr_code_type(self, sign_up_fixture, language):
        self.qr_creation_page.facebook_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_instagram_qr_code_type(self, sign_up_fixture, language):
        self.qr_creation_page.instagram_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_social_media_qr_code_type(self, sign_up_fixture, language):
        self.qr_creation_page.social_media_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    @pytest.mark.parametrize("language", languages_urls.keys())
    def test_whatsapp_qr_code_type(self, sign_up_fixture, language):
        self.qr_creation_page.whatsapp_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
