from base.base_page import BasePage


class QrCreationLocators:
    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        # QR Code Types From Step 1 screen
        self.step1_breadcrumbs_section_to_verify_page = self.base.locator("//span[@id='tab1text']")
        self.menu_burger_button = self.base.locator("//div[@id='openMenu']")
        self.website_qr_type = self.base.locator("//input[@data-qr_type='Url']/../../..")
        self.pdf_qr_type = self.base.locator("//input[@value='pdf']/../../..")
        self.links_qr_type = self.base.locator("//input[@value='links']/../../..")
        self.vcard_qr_type = self.base.locator("//input[@value='vcard']/../../..")
        self.business_qr_type = self.base.locator("//input[@value='business']/../../..")
        self.images_qr_type = self.base.locator("//input[@value='images']/../../..")
        self.video_qr_type = self.base.locator("//input[@value='video']/../../..")
        self.apps_qr_type = self.base.locator("//input[@value='app']/../../..")
        self.coupon_qr_type = self.base.locator("//input[@value='coupon']/../../..")
        self.mp3_qr_type = self.base.locator("//input[@value='mp3']/../../..")
        self.menu_qr_type = self.base.locator("//input[@value='menu']/../../..")
        self.wifi_qr_type = self.base.locator("//input[@value='wifi']/../../..")
        self.facebook_qr_type = self.base.locator("//input[@value='facebook']/../../..")
        self.instagram_qr_type = self.base.locator("//input[@value='instagram']/../../..")
        self.social_media_qr_type = self.base.locator("//input[@value='social']/../../..")
        self.whatsapp_qr_type = self.base.locator("//input[@value='whatsapp']/../../..")
        self.cross_close_btn = self.base.locator("//button[@id='closeBtn']")

        # Common Locators from Step 2 screen
        self.back_button = self.base.locator("//button[@id='cancel']")
        self.next_button = self.base.locator("//button[@id='temp_next']")
        self.modal_window_step2 = "//div[@id='helpCarousel']"
        self.help_modal_close_button = self.base.locator("//div[@id='helpCarousel']//button[@id='closeBtn']")
        # QR code name
        self.custom_name_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_nameOfQrCode']")
        self.custom_name_qr_code_input = self.base.locator("//input[@id='name']")
        # QR code password
        self.setup_password_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_password']")
        self.password_checkbox = self.base.locator("//input[@id='passcheckbox']")
        self.password_qr_code_input_field = self.base.locator("//input[@id='passwordField']")
        # QR code folder
        self.setup_new_folder_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_folder']")
        self.select_folder_title_dropdown = self.base.locator("//input[@id='folder_title']")
        self.create_new_folder_button = self.base.locator("//button[@id='createFolderBtn']")
        # QR code fonts
        self.update_fonts_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_nameOfFonts']")
        self.fonts_title_dropdown = self.base.locator(
            "//div[@id='dropdown_title']/../div/button[@class='drp-icon-btn-open']")
        self.fonts_texts_dropdown = self.base.locator("//div[@id='dropdown_text']/../div/button[@class='drp-icon-btn-open']")
        # QR code welcome screen
        self.upload_welcome_screen_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_welcomeScreen']")
        self.upload_welcome_screen_qr_code_input = self.base.locator("//input[@id='screen']")
        # QR code color theme
        self.update_color_theme_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_Design']")
        # QR code social networks
        self.social_network_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_social']")
        # Add list of social networks
        self.social_network_url_input = self.base.locator("//input[@id='socialUrl']")
        self.social_network_text_input = self.base.locator("//input[@name='social_icon_text[]']")
        # QR code contact details
        self.contact_details_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_contactInfo']")
        self.contact_details_contact_name = self.base.locator("//input[@id='contactName']")
        # add phone
        self.contact_details_qr_code_add_phone_btn = self.base.locator("//button[@id='addPhone']")
        self.contact_details_qr_code_add_phone_label = self.base.locator("//input[@id='vcard_phoneLabel']")
        self.contact_details_qr_code_add_phone_number = self.base.locator("//input[@id='vcard_phone']")
        self.contact_details_qr_code_delete_phone_btn = self.base.locator(
            "//div[@id='phoneBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add email
        self.contact_details_qr_code_add_email_btn = self.base.locator("//button[@id='addEmail']")
        self.contact_details_qr_code_add_email_label = self.base.locator("//input[@id='vcard_emailLabel']")
        self.contact_details_qr_code_add_email_address = self.base.locator("//input[@id='vcard_email']")
        self.contact_details_qr_code_delete_email_btn = self.base.locator(
            "//div[@id='emailBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add website
        self.contact_details_qr_code_add_website_btn = self.base.locator("//button[@id='addWebsite']")
        self.contact_details_qr_code_add_website_label = self.base.locator("//input[@id='vcard_website_title']")
        self.contact_details_qr_code_add_website_url = self.base.locator("// input[ @id='vcard_website']")
        self.contact_details_qr_code_delete_email_btn = self.base.locator(
            "//div[@id='websiteBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add location
        self.location_qr_code_dropdown = self.base.locator("//button[@data-target='#add_website-dis']")
        self.location_qr_code_search_address = self.base.locator("//input[@id='ship-address1']")
        # add button
        self.add_button_with_link = self.base.locator("//button[@id='add']")
        self.add_button_with_link_name = self.base.locator("//input[@id='businessButtons']")
        self.add_button_with_link_url = self.base.locator("//input[@id='businessButtonUrls']")
        # add button2
        self.add_button2_image_with_link = self.base.locator("//button[@id='add2']")
        self.add_button2_image_text_input = self.base.locator("//input[@id='button_text']")
        self.add_button2_image_url_input = self.base.locator("//input[@id='button_url']")

        # opening hours
        self.monday_checkbox = self.base.locator("//input[@id='checkboxMon']")
        self.monday_time_from = self.base.locator("#Monday_From")
        self.monday_time_to = self.base.locator("#Monday_To")

        # Website QR code locators
        self.setup_website_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_nameOfUrl']")
        self.setup_website_qr_code_input = self.base.locator("//input[@id='url']")

        # PDF QR code locators
        self.upload_pdf_qr_type_dropdown = self.base.locator("//button[@data-target='#acc_nameOfQrPdf']")
        self.upload_pdf_qr_type_button = self.base.locator("//div[@id='pdf']")
        self.upload_pdf_qr_type_drop_area = self.base.locator("#pdf")
        self.directly_show_pdf_checkbox = self.base.locator("//input[@id='direct_pdf']/following-sibling::label")
        self.add_pdf_information_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_pdfInformation']")
        self.company_pdf_info_input = self.base.locator("//input[@id='company']")
        self.title_pdf_info_input = self.base.locator("//input[@id='pdftitle']")
        self.description_pdf_info_input = self.base.locator("//textarea[@id='description']")
        self.website_pdf_info_input = self.base.locator("//input[@id='website']")
        self.button_pdf_info_input = self.base.locator("//input[@id='button']")

        # Links QR code locators
        self.basic_info_links_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_listInfo']")
        self.basic_info_links_qr_code_image_input = self.base.locator("//input[@id='companyLogo']")


        #self.basic_info_links_qr_code_image_input = "//input[@id='companyLogo']"
        self.basic_info_company_logo_input = self.base.locator("//input[@id='companyLogo']")

        self.basic_info_links_qr_code_title_input = self.base.locator("//input[@id='list_title']")
        self.basic_info_links_qr_code_description_input = self.base.locator("//textarea[@id='list_description']")
        self.list_of_links_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_link']")
        self.list_of_links_qr_code_delete_button = self.base.locator("//div[@class='links-delete-wrap']/button")
        self.list_of_links_qr_code_image_input = self.base.locator("//input[@id='linkImages1']")
        self.list_of_links_qr_code_link_text_input = self.base.locator("//input[@id='list_text']")
        self.list_of_links_qr_code_link_url_input = self.base.locator("//input[@id='list_URL']")
        self.links_qr_code_social_network_url_input = self.base.locator("//input[@id='socialUrl']")
        self.links_qr_code_social_network_text_input = self.base.locator("//input[@name='social_icon_text[]']")

        # Vcard QR code locators
        self.v_card_qr_code_image_input = self.base.locator("//input[@id='companyLogo']")
        self.v_card_qr_code_first_name_input = self.base.locator("//input[@id='vcard_first_name']")
        self.v_card_qr_code_last_name_input = self.base.locator("//input[@id='vcard_last_name']")
        self.v_card_qr_code_company_details_dropdown = self.base.locator("//button[@data-target='#acc_companyInfo']")
        self.v_card_qr_code_company_details_company_input = self.base.locator("//input[@id='vcard_company']")
        self.v_card_qr_code_company_details_profession_input = self.base.locator("//input[@id='vcard_profession']")
        self.v_card_qr_code_company_details_summary_input = self.base.locator("//textarea[@id='vcard_note']")

        # Business QR code locators
        self.business_info_business_qr_type_image_input = self.base.locator("//input[@id='companyLogo']")
        self.business_info_business_qr_type_company_input = self.base.locator("//input[@id='company']")
        self.business_info_business_qr_type_title_input = self.base.locator("//input[@id='companyTitle']")
        self.business_info_business_qr_type_subtitle_input = self.base.locator("//input[@id='companySubtitle']")
        self.business_info_business_qr_type_add_button = self.base.locator("//button[@id='add']")
        self.about_company_business_qr_type_dropdown = self.base.locator("//textarea[@id='aboutCompany']")
        self.about_company_business_qr_type_textarea = self.base.locator("//textarea[@id='aboutCompany']")

        # Images QR code locators
        self.upload_image_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_images']")
        self.upload_image_qr_code_button = self.base.locator("//div[@id='files']")
        self.upload_image_qr_code_drop_area = self.base.locator("#files")
        self.vertical_image_qr_code_checkbox = self.base.locator("//input[@id='uploadCheckbox']")
        self.image_information_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_imageInfo']")
        self.image_information_qr_code_gallery_title_input = self.base.locator("//input[@id='image_title']")
        self.image_information_qr_code_gallery_description_input = self.base.locator("//textarea[@id='image_description']")
        self.image_information_qr_code_website_input = self.base.locator("//input[@id='website']")

        # Video QR code locators
        self.upload_video_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_videoUpload']")
        self.upload_video_qr_code_url_input = self.base.locator("//input[@id='youTubeUrl']")
        self.upload_video_qr_code_button = self.base.locator("//div[@id='files']//button")
        self.upload_video_qr_code_drop_area = self.base.locator("#files")
        self.video_show_directly_qr_code_checkbox = self.base.locator("//input[@id='direct_video']")
        self.video_info_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_contactInfo']")
        self.video_info_qr_code_company_input = self.base.locator("//input[@id='companyName']")
        self.video_info_qr_code_video_title_input = self.base.locator("//input[@id='videoTitle']")
        self.video_info_qr_code_video_description_input = self.base.locator("//textarea[@id='videoDescription']")

        # Apps QR code locators
        self.app_info_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_imageInfo']")
        self.app_info_qr_code_app_name_input = self.base.locator("//input[@id='app_title']")
        self.app_info_qr_code_dev_company_input = self.base.locator("//input[@id='app_company']")
        self.app_info_qr_code_logo_img_input = self.base.locator("//input[@id='companyLogo']")
        self.app_info_qr_code_description_input = self.base.locator("//textarea[@id='app_description']")
        self.app_info_qr_code_website_input = self.base.locator("//input[@id='app_website']")
        self.links_to_platforms_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_imageInfo']")
        self.links_to_platforms_qr_code_google_add_button = self.base.locator("//button[contains(@class,'google_btn')]")
        self.links_to_platforms_qr_code_google_input = self.base.locator("//input[@id='google']")
        self.links_to_platforms_qr_code_apple_add_button = self.base.locator("//button[contains(@class,'apple_btn')]")
        self.links_to_platforms_qr_code_apple_input = self.base.locator("//input[@id='apple']")
        self.links_to_platforms_qr_code_amazon_add_button = self.base.locator("//button[contains(@class,'amazone_btn')]")
        self.links_to_platforms_qr_code_amazon_input = self.base.locator("//input[@id='amazon']")

        # Coupon QR code locators
        self.offer_info_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_imageInfo']")
        self.offer_info_qr_code_img_input = self.base.locator("//input[@id='companyLogo']")
        self.offer_info_qr_code_company_input = self.base.locator("//input[@id='company']")
        self.offer_info_qr_code_title_input = self.base.locator("//input[@id='title']")
        self.offer_info_qr_code_description_input = self.base.locator("//textarea[@id='description']")
        self.offer_info_qr_code_badge_input = self.base.locator("//input[@id='salesBadge']")
        self.offer_info_qr_code_see_code_button = self.base.locator("//input[@id='buttonToSeeCode']")
        self.coupon_info_qr_code_dropdown = self.base.locator("//button[@data-target='#acc_couponInfo']")
        self.coupon_info_qr_code_barcode_toggle = self.base.locator("//input[@id='couponTgl']")
        self.coupon_info_qr_code_code_input = self.base.locator("//input[@id='couponCode']")
        self.coupon_info_qr_code_terms_input = self.base.locator("//textarea[@id='terms']")
        self.coupon_info_qr_code_button_input = self.base.locator("//input[@id='buttonText']")
        self.coupon_info_qr_code_website_input = self.base.locator("//input[@id='buttonUrl']")

        # Mp3 QR code locators
        self.mp3_upload_dropdown = self.base.locator("//button[@data-target='#acc_nameOfMp3']")
        self.mp3_upload_add_option_checkbox = self.base.locator("//input[@id='addDownloadOption']")
        self.mp3_info_img_input = self.base.locator("//input[@id='companyLogo']")
        self.mp3_info_title_input = self.base.locator("//input[@id='mp3_title']")
        self.mp3_info_description_input = self.base.locator("//textarea[@id='mp3_description']")
        self.mp3_info_website_input = self.base.locator("//input[@id='mp3_website']")
        self.mp3_info_add_button = self.base.locator("//div[@id='btn-item']")
        self.mp3_info_button_text_input = self.base.locator("//input[@id='button_text']")
        self.mp3_info_button_website_input = self.base.locator("//input[@id='button_url']")
        self.mp3_info_button_remove_button = self.base.locator("//div[@id='add-btn']//button[contains(@class,'removeBtn')]")

        # Menu QR code locators
        self.menu_var_popup_modal_title = self.base.locator("//div[@id='helpCarousel1']//h5")
        self.menu_var_popup_menu_type_button = self.base.locator("//div[@id='menuModal']//button[@value='menu']")
        self.menu_var_popup_pdf_type_button = self.base.locator("//div[@id='menuModal']//button[@value='pdf']")
        self.menu_var_popup_web_type_button = self.base.locator("//div[@id='menuModal']//button[@value='url']")
        self.menu_var_popup_cross_button = self.base.locator("//div[@id='menuModal']//button[@value='url']")
        self.menu_menu_type_restaurant_dropdown = self.base.locator("//button[@data-target='#acc_menuInfo']")
        self.menu_menu_type_restaurant_img_input = self.base.locator("//input[@id='companyLogo']")
        self.menu_menu_type_restaurant_name_input = self.base.locator("//input[@id='companyTitle']")
        self.menu_menu_type_restaurant_description_input = self.base.locator("//textarea[@id='companyDescription']")
        self.menu_menu_type_menu_dropdown = self.base.locator("//button[@data-target='#acc_product']")
        self.menu_menu_type_section1_dropdown = self.base.locator(
            "//div[@id='add_section']//button[contains(@class,'section-btn') and @data-target='#menu_section_1']")
        self.menu_menu_type_section1_name_input = self.base.locator("//input[@id='sectionNames']")
        self.menu_menu_type_section1_description_of_section_input = self.base.locator("//input[@id='sectionDescriptions']")
        self.menu_menu_type_section1_image_input = self.base.locator("//input[@id='productImages1']")
        self.menu_menu_type_section1_product_name_input = self.base.locator(
            "//div[@class='row']//input[contains(@name,'productNames') and contains(@class,'pName')]")
        self.menu_menu_type_section1_name_translated_input = self.base.locator("//input[@id='productNamesTranslated']")
        self.menu_menu_type_section1_description_input = self.base.locator("//input[@id='productDescriptions']")
        self.menu_menu_type_section1_price_input = self.base.locator("//input[@id='productPrices']")
        # add allergens
        self.menu_link_type_url_input = self.base.locator("//input[@id='url']")

        # Wifi QR code locators
        self.wi_fi_info_dropdown = self.base.locator("//button[@data-target='#acc_WiFi_Information']")
        self.wi_fi_info_network_name_input = self.base.locator("//input[@id='wifi_ssid']")
        self.wi_fi_info_network_password_input = self.base.locator("//input[@id='wifi_password']")
        self.wi_fi_info_encrypting_type_dropdown = self.base.locator("//select[@id='wifi_encryption']")

        # Facebook QR code locators
        self.facebook_design_dropdown = self.base.locator("//button[@data-target='#facebook-bg']")
        self.facebook_design_image0 = self.base.locator("//div[@id='facebook-bg']//div[@data-image_id='0']")
        self.facebook_design_image1 = self.base.locator("//div[@id='facebook-bg']//div[@data-image_id='1']")
        self.facebook_design_image2 = self.base.locator("//div[@id='facebook-bg']//div[@data-image_id='2']")
        self.facebook_design_background_input = self.base.locator("//input[@id='fbBgImage']")
        self.facebook_profile_img_dropdown = self.base.locator("//button[@data-target='#facebook-profile']")
        self.facebook_profile_img_input = self.base.locator("//input[@id='companyLogo']")
        self.facebook_basic_info_dropdown = self.base.locator("//button[@data-target='#facebook-details']")
        self.facebook_basic_info_facebook_url = self.base.locator("//input[@id='facebook_url']")
        self.facebook_basic_info_facebook_title = self.base.locator("//input[@id='facebook_title']")
        self.facebook_basic_info_facebook_description = self.base.locator("//textarea[@id='facebook_description']")

        # Instagram QR code locators
        self.instagram_basic_info_dropdown = self.base.locator("//button[@data-target='#instagram_username']")
        self.instagram_basic_info_username_input = self.base.locator("//input[@id='inst_username']")

        # Social Media QR code locators
        self.social_media_design_dropdown = self.base.locator("//button[@data-target='#acc_Design']")
        self.social_media_basic_info_dropdown = self.base.locator("//button[@data-target='#social-media']")
        self.social_media_basic_info_title = self.base.locator("//input[@id='social_title']")
        self.social_media_basic_info_description = self.base.locator("//textarea[@id='social_description']")
        self.social_media_basic_info_description = self.base.locator("//textarea[@id='social_description']")

        # Whatsapp QR code locators
        self.whats_app_information_country_code_button = self.base.locator("//button[@class='iti__selected-country']")
        self.whats_app_information_us_code_option = self.base.locator("//li[@id='iti-0__item-us']")
        self.whats_app_information_dropdown = self.base.locator("//button[@data-target='#whatsapp_no']")
        self.whats_app_information_phone_input = self.base.locator("//input[@id='phone']")
        self.whats_app_information_message_input = self.base.locator("//textarea[@id='whatsapp_body']")

        # Step 3 locators
        self.frame_step3_dropdown = self.base.locator("//button[@data-target='#acc_frame']")
        self.qrcode_patterns_step3_dropdown = self.base.locator("//button[@data-target='#acc_patterns']")
        self.qrcode_corners_step3_dropdown = self.base.locator("//button[@data-target='#acc_corners']")
        self.qrcode_add_logo_step3_dropdown = self.base.locator("//button[@data-target='#acc_addLogo']")
        self.qrcode_upload_logo_input = self.base.locator("//input[@id='qr_code_logo']")
        self.create_button = self.base.locator("#temp_submit")
        self.back_button = self.base.locator("//button[@id='cancel']")
        self.close_download_modal_button = self.base.locator("//div[@id='DownloadModal']//button[@aria-label='Close']")
        # Add QR design parameters Frame, QR code pattern, QR code corners, Add logo.

        # DPF Download locators

        # DPF QR code pricing
        self.days_14_limited_access_button = self.base.locator("//input[@id='dpfPlan1']")
        self.days_14_full_access_button = self.base.locator("//input[@id='dpfPlan2']")
        self.annual_plan_button = self.base.locator("//input[@id='dpfPlan3']")
        self.continue_user_plan_button = self.base.locator("//a[@id='user_plan_url']")

        # DPF Download locators
        self.dpf_form_title = self.base.locator("//form[@id='register-dpf-form']/div[@class='-form-title']")
        self.dpf_form_email_input = self.base.locator("//input[@id='input-email']")
        self.dpf_form_submit_button = self.base.locator("//button[contains(@class,'-btn-submit')]")

        # DPF Congratulations modal window
        self.congrats_title_h2 = self.base.locator("//div[@class='thank-you']/h2")
        self.congrats_download_button = self.base.locator("//div[@class='thank-you']/div[@class='thank-btn-area']/a")
