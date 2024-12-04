import os
import allure
from PIL import Image
from utils.comparison_module import allure_attach_image_diff
import pytest
from base.base_test import BaseTest
from config import languages, qr_create_methods


@pytest.mark.parametrize("language", languages)
@allure.feature(f"Frame comparatives - {os.getenv('BROWSER')}")
@pytest.mark.skip("Fix is not ready yet")
class TestFrameComparatives(BaseTest):

    @pytest.mark.parametrize("qr_create_method", qr_create_methods)
    @allure.title(f"Comparative mobile preview and web view - {os.getenv('BROWSER')}")
    def test_comparative_preview_and_view(self, sign_up_fixture, browser, request, qr_create_method):
        test_func = request.node.originalname
        expected_image_path = (f"artifacts/snapshots/preview/Expected/{test_func}"
                               f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}].png")
        actual_image_path = (f"artifacts/snapshots/preview/Actual/{test_func}"
                             f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}].png")
        diff_image_path = (f"artifacts/snapshots/preview/Diff/{test_func}"
                           f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}].png")
        self.qr_creation_page.helper.set_screenshot_path(expected_image_path)
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        self.qr_creation_page.helper.take_iframe_screenshot()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.close_download_modal_button.click()
        with Image.open(expected_image_path) as img:
            width, height = img.size
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.header_create_qr_code_button).to_be_visible()
        new_page = self.my_qr_codes_page.open_in_new_tab(self.my_qr_codes_page.open_last_qr_link())
        new_page.set_viewport_size({"width": width, "height": height})
        new_page.wait_for_timeout(10000)
        new_page.locator("body").press("ControlOrMeta+.")
        new_page.add_style_tag(content="""
        .App {
            background: white !important;
        }
        """)
        new_page.screenshot(full_page=True, path=actual_image_path)
        allure_attach_image_diff(actual_image_path, expected_image_path, diff_image_path)