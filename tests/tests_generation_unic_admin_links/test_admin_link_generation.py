import os
import random
import allure
import pytest
from base.base_test import BaseTest
from config import get_env

refund_alert_text = "The refund was successfully completed."


@allure.epic("Admin Portal")
@allure.feature(f"Admin Payment Link Management - {os.getenv('BROWSER')}")
class TestAdminLinkGeneration(BaseTest):

    @allure.story("Payment Link Generation")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        """
    Test creation of unique payment links with different discount options.
    Steps:
    1. Create a QR code
    2. Log out and log in to admin panel
    3. Search for user and generate discount URL
    4. Open generated link and select a plan
    5. Fill billing information and make payment
    6. Verify successful payment
    """
    )
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "discount_button_locator",
        [
            "default_pricing_button",
            "discount_70_promo_button",
            "discount_8_99_monthly_button",
            "discount_50_one_time_button",
        ],
    )
    @allure.title("Create unique payment link with {discount_button_locator}")
    def test_admin_create_uniq_payment_link(
        self, sign_up_fixture, discount_button_locator, fake_email
    ):
        with allure.step("Create QR code"):
            discount_locator = getattr(self.admin_page.locator, discount_button_locator)
            self.qr_creation_page.website_qr_create()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()
            self.my_qr_codes_page.locator.download_modal_close_button.click()

        with allure.step("Log out and log in to admin panel"):
            self.menu_page.locator.my_account.click()
            self.my_account_page.locator.log_out_button.click()
            self.my_account_page.open_page(get_env("STAGE_ADMIN_LINK"))
            self.admin_page.checked_locator(
                self.admin_page.locator.admin_email_input
            ).fill(get_env("STAGE_ADMIN_EMAIL"))
            self.admin_page.locator.admin_log_in_button.click()
            self.admin_page.locator.admin_password_input.fill(
                get_env("STAGE_ADMIN_PASSWORD")
            )
            self.admin_page.locator.admin_log_in_button.click()

        with allure.step("Generate discount URL"):
            self.admin_page.locator.global_search_input.fill(fake_email)
            self.admin_page.locator.search_button.click()
            self.admin_page.get_user_menu_dots_button_users_tab(fake_email).click()
            self.admin_page.locator.generate_discount_url_btn.click()
            discount_locator.click()
            self.admin_page.locator.generate_link_button.click()
            link_text = self.admin_page.locator.generated_link.inner_text()
            self.admin_page.locator.pricing_popup_close_button.click()

        with allure.step("Log out from admin panel"):
            self.admin_page.locator.admin_logout_area.click()
            self.admin_page.locator.admin_logout_button.click()

        with allure.step("Open generated link and select plan"):
            self.main_page.open_page(link_text)
            self.plan_and_prices_page.locator.variable_plan_button_universal_locator.first.click(
                force=True
            )

        with allure.step("Fill billing information"):
            self.payment_page.locator.billing_full_name_input.fill("John Smit")
            self.payment_page.locator.billing_address_line1_input.fill(
                "ser John Smit st."
            )
            self.payment_page.locator.billing_city_input.fill("LA")
            options = self.payment_page.locator.billing_oblast_input.locator(
                "option"
            ).all()
            available_options = [
                option for option in options if not option.is_disabled()
            ]
            if available_options:
                random_option = random.choice(available_options)
                value = random_option.get_attribute("value")
                self.payment_page.locator.billing_oblast_input.select_option(value)
            self.payment_page.locator.billing_postal_code_input.fill("37800")
            self.payment_page.locator.billing_info_continue_button.click()

        with allure.step("Make payment"):
            self.payment_page.make_payment()
            self.payment_page.click_on_submit_payment_button()

        with allure.step("Verify successful payment"):
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.congrats_download_button
            )

    @allure.story("Refund Management")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        """
    This test verifies the full refund functionality in the admin panel with different subscription handling options.
    Steps:
    1. Create a QR code and complete a payment
    2. Log in to the admin panel
    3. Navigate to the payments section
    4. Initiate a full refund with specified subscription handling
    5. Verify the refund confirmation

    The test checks two scenarios:
    - Full refund with cancellation of subscription
    - Full refund while keeping the subscription active

    This ensures that admins can process full refunds correctly and manage subscriptions as needed.
    """
    )
    @pytest.mark.parametrize(
        "refund_button",
        [
            "full_refund_plan_button_cancel_subscription",
            "full_refund_plan_button_keep_subscription",
        ],
    )
    @allure.title("Process full refund: {refund_button}")
    def test_admin_full_refund_options(
        self, navigate_to_dpf_page, refund_button, fake_email
    ):
        with allure.step("Create QR code and complete payment"):
            self.qr_creation_page.website_qr_create()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_email_input
            ).fill(fake_email)
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_submit_button
            ).click()
            self.qr_creation_page.select_dpf_plan()
            self.payment_page.make_payment()
            self.payment_page.select_country_and_zip_in_payment_frame()
            self.payment_page.click_on_submit_payment_button()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.congrats_download_button
            ).click()
            self.my_qr_codes_page.locator.download_modal_close_button.click()

        with allure.step("Log out and log in to admin panel"):
            self.menu_page.locator.my_account.click()
            self.my_account_page.locator.log_out_button.click()
            self.my_account_page.open_page(get_env("STAGE_ADMIN_LINK"))
            self.admin_page.checked_locator(
                self.admin_page.locator.admin_email_input
            ).fill(get_env("STAGE_ADMIN_EMAIL"))
            self.admin_page.locator.admin_log_in_button.click()
            self.admin_page.locator.admin_password_input.fill(
                get_env("STAGE_ADMIN_PASSWORD")
            )
            self.admin_page.locator.admin_log_in_button.click()

        with allure.step("Navigate to payments section and initiate refund"):
            self.admin_page.locator.menu_payments_button.click()
            self.admin_page.get_user_menu_dots_button_payments_tab(fake_email).click()
            self.admin_page.get_user_menu_refund_button_payments_tab(fake_email).click()
            getattr(self.admin_page.locator, refund_button).click()
            self.admin_page.locator.refund_confirm_button_payments_tab.click()

        with allure.step("Verify refund confirmation"):
            self.admin_page.expect(
                self.admin_page.locator.refund_alert_message
            ).to_be_visible(timeout=10000)
            self.admin_page.expect(
                self.admin_page.locator.refund_alert_message
            ).to_have_text(refund_alert_text)

    @allure.story("Refund Management")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        """
    This test verifies the partial refund functionality in the admin panel.
    It includes the following steps:
    1. Create a QR code and complete a payment
    2. Log in to the admin panel
    3. Locate the user's payment
    4. Initiate a partial refund
    5. Verify the refund confirmation

    The test checks two scenarios:
    - Partial refund with cancellation of subscription
    - Partial refund while keeping the subscription active

    This ensures that admins can process partial refunds correctly 
    and manage subscriptions as needed.
    """
    )
    @pytest.mark.parametrize(
        "refund_button",
        [
            "partial_refund_plan_button_cancel_subscription",
            "partial_refund_plan_button_keep_subscription",
        ],
    )
    @allure.title("Process partial refund: {refund_button}")
    def test_admin_partial_refund_options(
        self, navigate_to_dpf_page, refund_button, fake_email
    ):
        with allure.step("Create QR code and complete payment"):
            self.qr_creation_page.website_qr_create()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.create_button
            ).click()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_email_input
            ).fill(fake_email)
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.dpf_form_submit_button
            ).click()
            self.qr_creation_page.select_dpf_plan()
            self.payment_page.make_payment()
            self.payment_page.select_country_and_zip_in_payment_frame()
            self.payment_page.click_on_submit_payment_button()
            self.qr_creation_page.checked_locator(
                self.qr_creation_page.locator.congrats_download_button
            ).click()
            self.my_qr_codes_page.locator.download_modal_close_button.click()

        with allure.step("Log out and log in to admin panel"):
            self.menu_page.locator.my_account.click()
            self.my_account_page.locator.log_out_button.click()
            self.my_account_page.open_page(get_env("STAGE_ADMIN_LINK"))
            self.admin_page.checked_locator(
                self.admin_page.locator.admin_email_input
            ).fill(get_env("STAGE_ADMIN_EMAIL"))
            self.admin_page.locator.admin_log_in_button.click()
            self.admin_page.locator.admin_password_input.fill(
                get_env("STAGE_ADMIN_PASSWORD")
            )
            self.admin_page.locator.admin_log_in_button.click()

        with allure.step("Navigate to payments section and initiate refund"):
            self.admin_page.locator.menu_payments_button.click()
            self.admin_page.get_user_menu_dots_button_payments_tab(fake_email).click()
            self.admin_page.get_user_menu_refund_button_payments_tab(fake_email).click()
            getattr(self.admin_page.locator, refund_button).click()
            self.admin_page.locator.refund_confirm_button_payments_tab.click()
            self.admin_page.locator.refund_amount_input_field.fill("2")
            self.admin_page.locator.refund_amount_input_payment_button.click()

        with allure.step("Verify refund confirmation"):
            self.admin_page.expect(
                self.admin_page.locator.refund_alert_message
            ).to_be_visible(timeout=10000)
            self.admin_page.expect(
                self.admin_page.locator.refund_alert_message
            ).to_have_text(refund_alert_text)
