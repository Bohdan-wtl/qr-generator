from random import Random
import pytest
from faker import Faker
from base.base_test import BaseTest
from config import languages_urls, languages_dpf_urls, get_env

refund_alert_text = "The refund was successfully completed."

@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestAdminLinkGeneration(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_faker(self):
        self.faker = Faker()
        self.random_number = Random().randint(3000, 3000000)
        self.fake_email = "wtl-automation" + str(self.random_number) + "@test.com"

    @pytest.fixture(scope='function')
    def sign_up_fixture(self, language):
        stage_url = languages_urls[language]
        self.main_page.open_page(stage_url)
        self.main_page.go_to_sign_up_page()
        self.register_page.sign_up(self.fake_email, "wtl-testBohdan@gmail.com")
        yield

    @pytest.fixture(scope='function')
    def navigate_to_dpf_page(self, dpf_language):
        stage_url = languages_dpf_urls[dpf_language]
        self.main_page.open_page(stage_url)

    @pytest.mark.flaky(reruns=0)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize("language", languages_urls.keys())
    @pytest.mark.parametrize("discount_button_locator", [
        "default_pricing_button",
        "discount_70_promo_button",
        "discount_8_99_monthly_button",
        "discount_50_one_time_button"
    ])
    def test_admin_create_uniq_payment_link(self, sign_up_fixture, discount_button_locator):
        discount_locator = getattr(self.admin_page.locator, discount_button_locator)
        self.qr_creation_page.website_qr_create()
        user_email = self.fake_email
        self.my_qr_codes_page.locator.download_modal_close_button.click()
        self.menu_page.locator.my_account.click()
        self.my_account_page.locator.log_out_button.click()
        self.my_account_page.open_page(get_env("STAGE_ADMIN_LINK"))
        self.admin_page.locator.admin_email_input.fill(get_env("STAGE_ADMIN_EMAIL"))
        self.admin_page.locator.admin_log_in_button.click()
        self.admin_page.locator.admin_password_input.fill(get_env("STAGE_ADMIN_PASSWORD"))
        self.admin_page.locator.admin_log_in_button.click()
        self.admin_page.locator.global_search_input.fill(user_email)
        self.admin_page.locator.search_button.click()
        self.admin_page.get_user_menu_dots_button_users_tab(user_email).click()
        self.admin_page.locator.generate_discount_url_btn.click()
        discount_locator.click()
        self.admin_page.locator.generate_link_button.click()
        link_text = self.admin_page.locator.generated_link.inner_text()
        self.admin_page.locator.pricing_popup_close_button.click()
        self.admin_page.locator.admin_logout_area.click()
        self.admin_page.locator.admin_logout_button.click()
        self.main_page.open_page(link_text)
        self.plan_and_prices_page.locator.variable_plan_button_universal_locator.first.click(force=True)
        self.payment_page.locator.billing_full_name_input.fill("John Smit")
        self.payment_page.locator.billing_address_line1_input.fill("ser John Smit st.")
        self.payment_page.locator.billing_city_input.fill("LA")
        self.payment_page.locator.billing_postal_code_input.fill("37800")
        self.payment_page.locator.billing_info_continue_button.click()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.wait_for(state="visible")
        self.qr_creation_page.expect(self.qr_creation_page.locator.congrats_download_button).to_be_visible()

    @pytest.mark.flaky(reruns=0)
    @pytest.mark.parametrize("dpf_language", languages_dpf_urls.keys())
    @pytest.mark.parametrize("refund_button", [
        "full_refund_plan_button_cancel_subscription",
        "full_refund_plan_button_keep_subscription"
    ])
    def test_admin_full_refund_options(self, navigate_to_dpf_page, refund_button):
        fake_email = self.fake_email
        self.qr_creation_page.website_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.locator.download_modal_close_button.click()
        self.menu_page.locator.my_account.click()
        self.my_account_page.locator.log_out_button.click()
        self.my_account_page.open_page(get_env("STAGE_ADMIN_LINK"))
        self.admin_page.locator.admin_email_input.fill(get_env("STAGE_ADMIN_EMAIL"))
        self.admin_page.locator.admin_log_in_button.click()
        self.admin_page.locator.admin_password_input.fill(get_env("STAGE_ADMIN_PASSWORD"))
        self.admin_page.locator.admin_log_in_button.click()
        self.admin_page.locator.menu_payments_button.click()
        self.admin_page.get_user_menu_dots_button_payments_tab(fake_email).click()
        self.admin_page.get_user_menu_refund_button_payments_tab(fake_email).click()
        getattr(self.admin_page.locator, refund_button).click()
        self.admin_page.locator.refund_confirm_button_payments_tab.click()
        self.admin_page.expect(self.admin_page.locator.refund_alert_message).to_be_visible(timeout=10000)
        self.admin_page.expect(self.admin_page.locator.refund_alert_message).to_have_text(refund_alert_text)

    @pytest.mark.flaky(reruns=0)
    @pytest.mark.parametrize("dpf_language", languages_dpf_urls.keys())
    @pytest.mark.parametrize("refund_button", [
        "partial_refund_plan_button_cancel_subscription",
        "partial_refund_plan_button_keep_subscription"
    ])
    def test_admin_partial_refund_options(self, navigate_to_dpf_page, refund_button):
        fake_email = self.fake_email
        self.qr_creation_page.website_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.locator.download_modal_close_button.click()
        self.menu_page.locator.my_account.click()
        self.my_account_page.locator.log_out_button.click()
        self.my_account_page.open_page(get_env("STAGE_ADMIN_LINK"))
        self.admin_page.locator.admin_email_input.fill(get_env("STAGE_ADMIN_EMAIL"))
        self.admin_page.locator.admin_log_in_button.click()
        self.admin_page.locator.admin_password_input.fill(get_env("STAGE_ADMIN_PASSWORD"))
        self.admin_page.locator.admin_log_in_button.click()
        self.admin_page.locator.menu_payments_button.click()
        self.admin_page.get_user_menu_dots_button_payments_tab(fake_email).click()
        self.admin_page.get_user_menu_refund_button_payments_tab(fake_email).click()
        getattr(self.admin_page.locator, refund_button).click()
        self.admin_page.locator.refund_confirm_button_payments_tab.click()
        self.admin_page.locator.refund_amount_input_field.fill("2")
        self.admin_page.locator.refund_amount_input_payment_button.click()
        self.admin_page.expect(self.admin_page.locator.refund_alert_message).to_be_visible(timeout=10000)
        self.admin_page.expect(self.admin_page.locator.refund_alert_message).to_have_text(refund_alert_text)
