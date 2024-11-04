from faker import Faker
from base.base_page import BasePage
from pages.locators.qr_creation_flow_locators import QrCreationLocators
from pages.qr_code_helper import QrCodeHelper


class QrCreationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = QrCreationLocators(page)
        self.faker = Faker()
        self.helper = QrCodeHelper(self.page, self.locator)

    # DPF Flow with select_dpf_plan function
    def select_dpf_plan(self):
        self.locator.annual_plan_button.click()
        self.locator.continue_user_plan_button.click()

    def pdf_qr_create(self):
        self.locator.pdf_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.wait_for_loader_disappear()
        self.page.wait_for_selector('#pdf')
        self.helper.emulate_drag_and_drop('#pdf', 'pdf')
        self.helper.select_random_colors()
        self.locator.company_pdf_info_input.fill(self.faker.company())
        self.locator.title_pdf_info_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.description_pdf_info_input.fill(self.faker.text(max_nb_chars=250))
        self.locator.website_pdf_info_input.fill(self.faker.url())
        self.locator.button_pdf_info_input.fill(self.faker.word())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="PDF")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.helper.select_pattern_step3()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.set_file(self.locator.qrcode_upload_logo_input, 'image')
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def coupon_qr_create(self):
        self.locator.coupon_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.locator.coupon_info_qr_code_code_input.fill('5859083434')
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def mp3_qr_create(self):
        self.locator.mp3_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.helper.emulate_drag_and_drop('#mp3', 'mp3')
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def menu_menu_qr_create(self):
        self.locator.menu_qr_type.click(delay=1000)  
        self.locator.menu_var_popup_menu_type_button.click()  
        self.helper.close_help_modal_window_st2()  
        self.locator.menu_menu_type_section1_name_input.fill("section name")  
        self.locator.menu_menu_type_section1_product_name_input.fill("menu name")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.helper.wait_for_loader_disappear()

    def menu_pdf_qr_create(self):
        self.locator.menu_qr_type.click(delay=1000)  
        self.locator.menu_var_popup_pdf_type_button.click()  
        self.helper.close_help_modal_window_st2()  
        self.helper.emulate_drag_and_drop('#pdf', 'pdf')
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def menu_link_qr_create(self):
        self.locator.menu_qr_type.click(delay=1000)  
        self.locator.menu_var_popup_link_type_button.click()  
        self.locator.menu_link_type_url_input.fill(self.faker.url())
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def wifi_qr_create(self):
        self.locator.wifi_qr_type.click(delay=1000)  
        self.locator.wi_fi_info_network_name_input.fill("Some wifi name")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def facebook_qr_create(self):
        self.locator.facebook_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.locator.facebook_basic_info_facebook_url.fill(
            "https://www.facebook.com/automation_test_example")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def instagram_qr_create(self):
        self.locator.instagram_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.locator.instagram_basic_info_username_input.fill(
            "insta_nickname")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def social_media_qr_create(self):
        self.locator.social_media_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.locator.social_media_basic_info_title.fill(
            "social_media_title")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def whatsapp_qr_create(self):
        self.locator.whatsapp_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.locator.whats_app_information_phone_input.fill("0501234567")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def video_qr_create(self):
        self.locator.video_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.helper.emulate_drag_and_drop('#files', 'mp4')
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def image_qr_create(self):
        self.locator.images_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#files', 'image')
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def apps_qr_create(self):
        self.locator.apps_qr_type.click(delay=1000)  
        self.helper.close_help_modal_window_st2()  
        self.locator.app_info_qr_code_app_name_input.fill('App name')  
        self.locator.links_to_platforms_qr_code_google_add_button.click()  
        self.locator.links_to_platforms_qr_code_google_input.fill(self.faker.url())
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)  
        self.helper.close_help_modal_window_st3()  
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def business_qr_create(self):
        self.locator.business_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.locator.business_info_business_qr_type_company_input.fill('Some First name')
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def vcard_qr_create(self):
        self.locator.vcard_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_colors()
        self.locator.v_card_qr_code_first_name_input.fill(self.faker.first_name())
        self.locator.v_card_qr_code_last_name_input.fill(self.faker.last_name())
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def links_qr_create(self):
        self.locator.links_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_colors()
        self.helper.set_file(self.locator.basic_info_links_qr_code_image_input, 'image')
        self.locator.basic_info_links_qr_code_title_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.basic_info_links_qr_code_description_input.fill(self.faker.text(max_nb_chars=270))
        self.locator.list_of_links_qr_code_link_text_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.list_of_links_qr_code_link_url_input.fill(self.faker.url())
        self.helper.select_random_social_network_option()
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Links")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.helper.select_pattern_step3()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.set_file(self.locator.qrcode_upload_logo_input, 'image')
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def website_qr_create(self):
        self.locator.website_qr_type.click(delay=1000)
        self.locator.setup_website_qr_code_input.fill(self.faker.url())
        self.locator.custom_name_qr_code_dropdown.click()
        self.helper.set_custom_qr_code_name(qr_code_type="Website")
        self.helper.take_iframe_screenshot()
        self.locator.next_button.click(delay=1000)
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click(delay=1000)
        self.helper.wait_for_loader_disappear()

    def set_screenshot_path(self, screenshot_path):
        self.helper.set_screenshot_path(screenshot_path)
