import time

import allure
from faker import Faker
from base.base_page import BasePage
from pages.locators.qr_creation_flow_locators import QrCreationLocators
from pages.qr_code_helper import QrCodeHelper
import random


class QrCreationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = QrCreationLocators(page)
        self.faker = Faker()
        self.helper = QrCodeHelper(self.page, self.locator)

    @allure.step("Select DPF plan")
    def select_dpf_plan(self):
        self.locator.annual_plan_button.click()
        self.locator.continue_user_plan_button.click()

    @allure.step("Click on Next button")
    def click_next_button_step2(self):
        self.locator.next_button.click()

    @allure.step("Complete step 3")
    def complete_step_3(self):
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.locator.qrcode_patterns_step3_dropdown.click()
        self.helper.select_random_child_by_attribute(
            '//div[@id="acc_patterns"]//div[contains(@class,"d-flex mb-3 qr-shape customScrollbar")]', 'label', 'id')
        self.locator.qrcode_corners_step3_dropdown.click()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.scroll_into_view_if_needed()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.set_file(self.locator.qrcode_upload_logo_input, 'image')


    @allure.step("Create Webiste QR code")
    def website_qr_create(self):
        self.locator.website_qr_type.click(delay=1000)
        self.locator.setup_website_qr_code_input.fill(self.faker.url())
        self.helper.set_custom_qr_code_name(qr_code_type="Website")
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.locator.qrcode_patterns_step3_dropdown.click()
        self.helper.select_random_child_by_attribute(
            '//div[@id="acc_patterns"]//div[contains(@class,"d-flex mb-3 qr-shape customScrollbar")]', 'label', 'id')
        self.locator.qrcode_corners_step3_dropdown.click()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.set_file(self.locator.qrcode_upload_logo_input, 'image')


    @allure.step("Create PDF QR code")
    def pdf_qr_create(self):
        self.locator.pdf_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#pdf', 'pdf')

        # self.locator.directly_show_pdf_checkbox.is_editable() # Directly show the PDF file - option
        # self.locator.directly_show_pdf_checkbox.click() # Directly show the PDF file - option

        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.locator.company_pdf_info_input.fill(self.faker.company())
        self.locator.title_pdf_info_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.description_pdf_info_input.fill(self.faker.text(max_nb_chars=200))
        self.locator.website_pdf_info_input.fill(self.faker.url())
        self.locator.button_pdf_info_input.fill(self.faker.word())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="PDF")

    @allure.step("Create Links QR code")
    def links_qr_create(self):
        self.locator.links_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.helper.set_file(self.locator.basic_info_links_qr_code_image_input, 'image')
        self.locator.basic_info_links_qr_code_title_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.basic_info_links_qr_code_description_input.fill(self.faker.text(max_nb_chars=270))
        self.locator.list_of_links_qr_code_link_text_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.list_of_links_qr_code_link_url_input.fill(self.faker.url())
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Links")

    @allure.step("Create VCard QR code")
    def vcard_qr_create(self):
        self.locator.vcard_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.locator.v_card_qr_code_first_name_input.fill(self.faker.first_name())
        self.locator.v_card_qr_code_last_name_input.fill(self.faker.last_name())
        self.helper.add_phone_email_website()
        self.helper.set_location()
        self.locator.v_card_qr_code_company_details_company_input.fill(self.faker.company())
        self.locator.v_card_qr_code_company_details_profession_input.fill(self.faker.word())
        self.locator.v_card_qr_code_company_details_summary_input.fill(self.faker.text(max_nb_chars=250))
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="vCard")

    @allure.step("Create Business QR code")
    def business_qr_create(self):
        self.locator.business_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.locator.business_info_business_qr_type_company_input.fill(self.faker.company())
        self.locator.business_info_business_qr_type_title_input.fill(self.faker.text(max_nb_chars=20))
        self.locator.business_info_business_qr_type_subtitle_input.fill(self.faker.text(max_nb_chars=50))
        self.locator.add_button_with_link.click()
        self.locator.add_button_with_link_name.fill(self.faker.word())
        self.locator.add_button_with_link_url.fill(self.faker.url())
        self.locator.monday_checkbox.check(force=True)
        self.page.evaluate("document.querySelector('#Monday_From').value = '08:00'")
        self.page.evaluate("document.querySelector('#Monday_To').value = '09:00'")
        self.helper.set_location()
        self.locator.contact_details_contact_name.fill(self.faker.name())
        self.helper.add_phone_email_website()
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.about_company_business_qr_type_textarea.fill(self.faker.text(max_nb_chars=100))
        self.helper.select_random_child_by_attribute('//div[@id="acc_facilities"]//ul', 'li', 'title')
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Business")

    @allure.step("Create Image QR code")
    def image_qr_create(self):
        self.locator.images_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.helper.emulate_drag_and_drop('#files', 'image')
        self.locator.image_information_qr_code_gallery_title_input.fill(self.faker.text(max_nb_chars=20))
        self.locator.image_information_qr_code_gallery_description_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.image_information_qr_code_website_input.fill(self.faker.url())
        self.locator.add_button2_image_with_link.click()
        self.locator.add_button2_image_text_input.fill(self.faker.word())
        self.locator.add_button2_image_url_input.fill(self.faker.url())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Business")

    @allure.step("Create Video QR code")
    def video_qr_create(self):
        self.locator.video_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#files', 'mp4')
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.locator.video_info_qr_code_company_input.fill(self.faker.company())
        self.locator.video_info_qr_code_video_title_input.fill(self.faker.text(max_nb_chars=30))
        self.locator.video_info_qr_code_video_description_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.add_button2_image_with_link.click()
        self.locator.add_button2_image_text_input.fill(self.faker.word())
        self.locator.add_button2_image_url_input.fill(self.faker.url())
        self.locator.social_network_qr_code_dropdown.click()
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Business")

    @allure.step("Create Apps QR code")
    def apps_qr_create(self):
        self.locator.apps_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.locator.app_info_qr_code_app_name_input.fill(self.faker.company())
        self.locator.app_info_qr_code_dev_company_input.fill(self.faker.company())
        self.helper.set_file(self.locator.app_info_qr_code_logo_img_input, 'image')
        self.locator.app_info_qr_code_description_input.fill(self.faker.text(max_nb_chars=200))
        self.locator.app_info_qr_code_website_input.fill(self.faker.url())
        self.locator.links_to_platforms_qr_code_google_add_button.click()
        self.locator.links_to_platforms_qr_code_google_input.fill(self.faker.url())
        self.locator.links_to_platforms_qr_code_apple_add_button.click()
        self.locator.links_to_platforms_qr_code_apple_input.fill(self.faker.url())
        self.locator.links_to_platforms_qr_code_amazon_add_button.click()
        self.locator.links_to_platforms_qr_code_amazon_input.fill(self.faker.url())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Apps")

    @allure.step("Create Coupon QR code")
    def coupon_qr_create(self):
        self.locator.coupon_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.helper.set_file(self.locator.offer_info_qr_code_img_input, 'image')
        self.locator.offer_info_qr_code_company_input.fill(self.faker.company())
        self.locator.offer_info_qr_code_title_input.fill(self.faker.text(max_nb_chars=20))
        self.locator.offer_info_qr_code_description_input.fill(self.faker.text(max_nb_chars=200))
        self.locator.offer_info_qr_code_badge_input.fill(self.faker.word())
        self.locator.offer_info_qr_code_see_code_button.fill(self.faker.word())
        self.locator.coupon_info_qr_code_code_input.fill('5859083434')
        self.locator.coupon_info_qr_code_terms_input.fill(self.faker.text(max_nb_chars=200))
        self.locator.coupon_info_qr_code_button_input.fill(self.faker.word())
        self.locator.coupon_info_qr_code_website_input.fill(self.faker.url())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Coupon")

    @allure.step("Create MP3 QR code")
    def mp3_qr_create(self):
        self.locator.mp3_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#mp3', 'mp3')
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.helper.set_file(self.locator.mp3_info_img_input, 'image')
        self.locator.mp3_info_title_input.fill(self.faker.text(max_nb_chars=20))
        self.locator.mp3_info_description_input.fill(self.faker.text(max_nb_chars=200))
        self.locator.mp3_info_website_input.fill(self.faker.url())
        self.locator.add_button_with_link.click()
        self.locator.add_button2_image_text_input.fill(self.faker.word())
        self.locator.add_button2_image_url_input.fill(self.faker.url())
        self.locator.social_network_qr_code_dropdown.click()
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="MP3")

    @allure.step("Create Menu QR code")
    def menu_digital_qr_create(self):
        self.locator.menu_qr_type.click(delay=1000)
        self.locator.menu_var_popup_menu_type_button.click()
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.helper.set_file(self.locator.menu_menu_type_restaurant_img_input, 'image')
        self.locator.menu_menu_type_restaurant_name_input.fill(self.faker.company())
        self.locator.menu_menu_type_restaurant_description_input.fill(self.faker.text(max_nb_chars=200))
        self.locator.menu_menu_type_section1_name_input.fill(self.faker.word())
        self.locator.menu_menu_type_section1_description_of_section_input.fill(self.faker.text(max_nb_chars=100))
        self.helper.set_file(self.locator.menu_menu_type_section1_image_input, 'image')
        self.locator.menu_menu_type_section1_product_name_input.fill(self.faker.word())
        self.locator.menu_menu_type_section1_name_translated_input.fill(self.faker.word())
        self.locator.menu_menu_type_section1_description_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.menu_menu_type_section1_price_input.fill(str(self.faker.random_int(min=2, max=100)))
        self.helper.select_random_child_by_attribute(
            '//div[@id="menu_product_1_1"]//div[contains(@class,"mt-1 row  mx-0  align-item-center all_allergens")]',
            'input', 'value')
        self.page.evaluate("document.querySelector('#Monday_From').value = '08:00'")
        self.page.evaluate("document.querySelector('#Monday_To').value = '09:00'")
        self.helper.add_phone_email_website()
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')  # BUG on click!
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Menu-Digital")

    @allure.step("Create Menu - PDF QR code")
    def menu_pdf_qr_create(self):
        self.locator.menu_qr_type.click(delay=1000)
        self.locator.menu_var_popup_pdf_type_button.click()
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#pdf', 'pdf')
        # self.locator.directly_show_pdf_checkbox.is_editable() # Directly show the PDF file - option
        # self.locator.directly_show_pdf_checkbox.click() # Directly show the PDF file - option

        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]', 'div', 'id')
        self.locator.company_pdf_info_input.fill(self.faker.company())
        self.locator.title_pdf_info_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.description_pdf_info_input.fill(self.faker.text(max_nb_chars=250))
        self.locator.website_pdf_info_input.fill(self.faker.url())
        self.locator.button_pdf_info_input.fill(self.faker.word())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Menu - PDF")

    @allure.step("Create Menu - Website QR code")
    def menu_link_qr_create(self):
        self.locator.menu_qr_type.click(delay=1000)
        self.locator.menu_var_popup_web_type_button.click()
        self.locator.setup_website_qr_code_input.fill(self.faker.url())
        self.helper.set_custom_qr_code_name(qr_code_type="Menu - Website")

        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.locator.qrcode_patterns_step3_dropdown.click()
        self.helper.select_random_child_by_attribute(
            '//div[@id="acc_patterns"]//div[contains(@class,"d-flex mb-3 qr-shape customScrollbar")]', 'label', 'id')
        self.locator.qrcode_corners_step3_dropdown.click()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.set_file(self.locator.qrcode_upload_logo_input, 'image')

    @allure.step("Create Wi-Fi QR code")
    def wifi_qr_create(self):
        self.locator.wifi_qr_type.click(delay=1000)
        self.locator.wi_fi_info_network_name_input.fill(self.faker.text(max_nb_chars=20))
        self.locator.wi_fi_info_network_password_input.fill(str(self.faker.text(max_nb_chars=8)))
        random_encryption_type = random.choice(["WPA", "WEP", "WPA/WPA2", "nopass"])
        self.locator.wi_fi_info_encrypting_type_dropdown.select_option(random_encryption_type)
        self.helper.set_custom_qr_code_name(qr_code_type="Wi-Fi")

    @allure.step("Create Facebook QR code")
    def facebook_qr_create(self):
        self.locator.facebook_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.set_file(self.locator.facebook_design_background_input, 'image')
        self.helper.set_file(self.locator.facebook_profile_img_input, 'image')
        self.locator.facebook_basic_info_facebook_url.fill(f"https://www.facebook.com/{self.faker.word()}")
        self.locator.facebook_basic_info_facebook_title.fill(self.faker.text(max_nb_chars=35))
        self.locator.facebook_basic_info_facebook_description.fill(self.faker.text(max_nb_chars=100))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Facebook")

    @allure.step("Create Instagram QR code")
    def instagram_qr_create(self):
        self.locator.instagram_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.locator.instagram_basic_info_username_input.fill(self.faker.user_name())
        self.helper.set_custom_qr_code_name(qr_code_type="Instagram")

    @allure.step("Create LinkedIn QR code")
    def social_media_qr_create(self):
        self.locator.social_media_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_child_by_attribute('//div[contains(@class,"colorPaletteForm row m-0")]',
                                                     'div', 'id')
        self.locator.social_media_basic_info_title.fill(self.faker.text(max_nb_chars=30))
        self.locator.social_media_basic_info_description.fill(self.faker.text(max_nb_chars=200))
        self.helper.emulate_drag_and_drop('#files', 'image')
        time.sleep(5)
        self.helper.select_random_child_by_attribute('//div[@class= "socialIconContain"]', 'button',
                                                     'id')
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Social Media")

    @allure.step("Create WhatsApp QR code")
    def whatsapp_qr_create(self):
        self.locator.whatsapp_qr_type.click(delay=1000)
        self.helper.close_help_modal_window_st2()
        self.locator.whats_app_information_country_code_button.click()
        self.locator.whats_app_information_us_code_option.scroll_into_view_if_needed()
        self.locator.whats_app_information_us_code_option.click()
        self.locator.whats_app_information_phone_input.fill(str(self.faker.random_int(min=1111111111, max=9999999999)))
        self.locator.whats_app_information_message_input.fill(self.faker.text(max_nb_chars=100))
        self.helper.set_custom_qr_code_name(qr_code_type="WhatsApp")
