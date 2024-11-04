from random import Random
import pytest
from faker import Faker
from base.base_test import BaseTest
from config import languages_urls


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
@pytest.mark.parametrize("languages", languages_urls.keys())
class TestDefaultSignUpFlow(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_faker(self):
        self.faker = Faker()
        self.random_number = Random().randint(1000, 3000)
        self.fake_email = "wtl-automation" + str(self.random_number) + "@test.com"

    @pytest.fixture(scope='function', autouse=True)
    def sign_up_fixture(self, languages):
        stage_url = languages_urls[languages]
        self.main_page.open_page(stage_url)
        self.main_page.go_to_sign_up_page()
        self.register_page.sign_up(self.fake_email, "wtl-testBohdan@gmail.com")
        yield

    def test_website_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.website_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_pdf_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.pdf_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_links_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.links_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_vcard_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.vcard_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_business_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.business_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_images_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.image_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_video_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.video_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_apps_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.apps_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_coupon_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.coupon_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_mp3_qr_code_create(self, sign_up_fixture):
        self.qr_creation_page.mp3_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_menu_qr_code_create_menu_type(self, sign_up_fixture):
        self.qr_creation_page.menu_menu_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_menu_qr_code_create_pdf_type(self, sign_up_fixture):
        self.qr_creation_page.menu_pdf_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_menu_qr_code_create_link_type(self, sign_up_fixture):
        self.qr_creation_page.menu_link_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_wi_fi_qr_code_type(self, sign_up_fixture):
        self.qr_creation_page.wifi_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_facebook_qr_code_type(self, sign_up_fixture):
        self.qr_creation_page.facebook_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_instagram_qr_code_type(self, sign_up_fixture):
        self.qr_creation_page.instagram_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_social_media_qr_code_type(self, sign_up_fixture):
        self.qr_creation_page.social_media_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()

    def test_whatsapp_qr_code_type(self, sign_up_fixture):
        self.qr_creation_page.whatsapp_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
