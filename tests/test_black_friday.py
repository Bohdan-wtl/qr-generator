import os
import time

import allure
import pytest
from base.base_test import BaseTest
from config import dev_languages_dpf_urls

@pytest.mark.parametrize(f"dev_languages", dev_languages_dpf_urls.keys())
@allure.feature(f"DPF sign up flow - {os.getenv('BROWSER')}")
class TestDPFSignUpFlow(BaseTest):

    @allure.title(f"QR type - {os.getenv('BROWSER')}")
    @pytest.mark.parametrize("qr_create_method", ["wifi_qr_create"
                                                  ])
    def test_dpf_sign_up_qr_type(self, navigate_to_dev_dpf_page, qr_create_method, fake_email, page, dev_languages):

        expected_discount_70_text = page.locator(".friday-text .color-text")
        expected_banner = page.locator(".black-friday-full-wrap.dpf-black-friday ")
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.locator.help_modal_close_button.is_visible()
        self.qr_creation_page.locator.help_modal_close_button.click()
        self.qr_creation_page.locator.create_button.click()

        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        actual_text = expected_discount_70_text.text_content()
        time.sleep(2)
        page.screenshot(path=f"blackfriday/desktop_webkit_dpf_flow_{dev_languages}.png", full_page=True)
        assert "70%" in actual_text, f"'70%' not found in text: '{actual_text}'"
