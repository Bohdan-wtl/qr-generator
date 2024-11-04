from random import Random
import pytest
from faker import Faker
from base.base_test import BaseTest
from config import languages_urls


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
@pytest.mark.parametrize("language", languages_urls.keys())
class TestSandBox(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_faker(self):
        self.faker = Faker()
        self.random_number = Random().randint(1000, 3000)
        self.fake_email = "wtl-automation" + str(self.random_number) + "@test.com"

    @pytest.fixture(scope='function', autouse=True)
    def sign_up_fixture(self, language):
        stage_url = languages_urls[language]
        self.main_page.open_page(stage_url)
        self.main_page.go_to_sign_up_page()
        self.register_page.sign_up(self.fake_email, "wtl-testBohdan@gmail.com")
        yield

    def test_coupon(self):
        self.qr_creation_page.menu_link_qr_create()

    def test_pdf_qr_create(self):
        self.qr_creation_page.pdf_qr_create()

    def test_mp3_qr_create(self):
        self.qr_creation_page.mp3_qr_create()

    def test_menu_menu_qr_create(self):
        self.qr_creation_page.menu_menu_qr_create()

    def test_menu_menu_pdf_qr_create(self):
        self.qr_creation_page.menu_pdf_qr_create()

    def test_menu_link_qr_create(self):
        self.qr_creation_page.menu_link_qr_create()

    def test_wifi_qr_create(self):
        self.qr_creation_page.wifi_qr_create()

    def test_facebook_qr_create(self):
        self.qr_creation_page.facebook_qr_create()

    def test_instagram_qr_create(self):
        self.qr_creation_page.instagram_qr_create()

    def test_social_media_qr_create(self):
        self.qr_creation_page.social_media_qr_create()

    def test_whatsapp_qr_create(self):
        self.qr_creation_page.whatsapp_qr_create()

    def test_video_qr_create(self):
        self.qr_creation_page.video_qr_create()

    def test_image_qr_create(self):
        self.qr_creation_page.image_qr_create()

    def test_apps_qr_create(self):
        self.qr_creation_page.apps_qr_create()

    def test_business_qr_create(self):
        self.qr_creation_page.business_qr_create()

    def test_vcard_qr_create(self):
        self.qr_creation_page.vcard_qr_create()

    def test_links_qr_create(self):
        self.qr_creation_page.links_qr_create()

    def test_website_qr_create(self):
        self.qr_creation_page.website_qr_create()