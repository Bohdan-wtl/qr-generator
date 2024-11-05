class QrCreationLocators:
    def __init__(self, page):
        # QR Code Types From Step 1 screen
        self.step1_breadcrumbs_section_to_verify_page = page.locator("//span[@id='tab1text']")
        self.menu_burger_button = page.locator("//div[@id='openMenu']")
        self.website_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Url']")
        self.pdf_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Pdf']")
        self.links_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Links']")
        self.vcard_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Vcard']")
        self.business_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Business']")
        self.images_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Images']")
        self.video_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Video']")
        self.apps_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='App']")
        self.coupon_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Coupon']")
        self.mp3_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Mp3']")
        self.menu_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Menu']")
        self.wifi_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Wifi']")
        self.facebook_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Facebook']")
        self.instagram_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Instagram']")
        self.social_media_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Social']")
        self.whatsapp_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Whatsapp']")
        self.cross_close_btn = page.locator("//button[@id='closeBtn']")

        # Common Locators from Step 2 screen
        self.back_button = page.locator("//button[@id='cancel']")
        self.next_button = page.locator("//button[@id='temp_next']")
        self.modal_window_step2 = "//div[@id='helpCarousel']"
        self.help_modal_close_button = page.locator("//div[@id='helpCarousel']//button[@id='closeBtn']")
        # QR code name
        self.custom_name_qr_code_dropdown = page.locator("//button[@data-target='#acc_nameOfQrCode']")
        self.custom_name_qr_code_input = page.locator("//input[@id='name']")
        # QR code password
        self.setup_password_qr_code_dropdown = page.locator("//button[@data-target='#acc_password']")
        self.password_checkbox = page.locator("//input[@id='passcheckbox']")
        self.password_qr_code_input_field = page.locator("//input[@id='passwordField']")
        # QR code folder
        self.setup_new_folder_qr_code_dropdown = page.locator("//button[@data-target='#acc_folder']")
        self.select_folder_title_dropdown = page.locator("//input[@id='folder_title']")
        self.create_new_folder_button = page.locator("//button[@id='createFolderBtn']")
        # QR code fonts
        self.update_fonts_qr_code_dropdown = page.locator("//button[@data-target='#acc_nameOfFonts']")
        self.fonts_title_dropdown = page.locator(
            "//div[@id='dropdown_title']/../div/button[@class='drp-icon-btn-open']")
        self.fonts_texts_dropdown = page.locator("//div[@id='dropdown_text']/../div/button[@class='drp-icon-btn-open']")
        # QR code welcome screen
        self.upload_welcome_screen_qr_code_dropdown = page.locator("//button[@data-target='#acc_welcomeScreen']")
        self.upload_welcome_screen_qr_code_input = page.locator("//input[@id='screen']")
        # QR code color theme
        self.update_color_theme_qr_code_dropdown = page.locator("//button[@data-target='#acc_Design']")
        # QR code social networks
        self.social_network_qr_code_dropdown = page.locator("//button[@data-target='#acc_social']")
        # Add list of social networks
        self.social_network_url_input = page.locator("//input[@id='socialUrl']")
        self.social_network_text_input = page.locator("//input[@name='social_icon_text[]']")
        # QR code contact details
        self.contact_details_qr_code_dropdown = page.locator("//button[@data-target='#acc_contactInfo']")
        self.contact_details_contact_name = page.locator("//input[@id='contactName']")
        # add phone
        self.contact_details_qr_code_add_phone_btn = page.locator("//button[@id='addPhone']")
        self.contact_details_qr_code_add_phone_label = page.locator("//input[@id='vcard_phoneLabel']")
        self.contact_details_qr_code_add_phone_number = page.locator("//input[@id='vcard_phone']")
        self.contact_details_qr_code_delete_phone_btn = page.locator(
            "//div[@id='phoneBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add email
        self.contact_details_qr_code_add_email_btn = page.locator("//button[@id='addEmail']")
        self.contact_details_qr_code_add_email_label = page.locator("//input[@id='vcard_emailLabel']")
        self.contact_details_qr_code_add_email_address = page.locator("//input[@id='vcard_email']")
        self.contact_details_qr_code_delete_email_btn = page.locator(
            "//div[@id='emailBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add website
        self.contact_details_qr_code_add_website_btn = page.locator("//button[@id='addWebsite']")
        self.contact_details_qr_code_add_website_label = page.locator("//input[@id='vcard_website_title']")
        self.contact_details_qr_code_add_website_url = page.locator("// input[ @id='vcard_website']")
        self.contact_details_qr_code_delete_email_btn = page.locator(
            "//div[@id='websiteBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add location
        self.location_qr_code_dropdown = page.locator("//button[@data-target='#add_website-dis']")
        self.location_qr_code_search_address = page.locator("//input[@id='ship-address1']")
        # add button
        self.add_button_with_link = page.locator("//button[@id='add']")
        self.add_button_with_link_name = page.locator("//input[@id='businessButtons']")
        self.add_button_with_link_url = page.locator("//input[@id='businessButtonUrls']")
        # add button2
        self.add_button2_image_with_link = page.locator("//button[@id='add2']")
        self.add_button2_image_text_input = page.locator("//input[@id='button_text']")
        self.add_button2_image_url_input = page.locator("//input[@id='button_url']")

        # opening hours
        self.monday_checkbox = page.locator("//input[@id='checkboxMon']")
        self.monday_time_from = page.locator("#Monday_From")
        self.monday_time_to = page.locator("#Monday_To")

        # Website QR code locators
        self.setup_website_qr_code_dropdown = page.locator("//button[@data-target='#acc_nameOfUrl']")
        self.setup_website_qr_code_input = page.locator("//input[@id='url']")

        # PDF QR code locators
        self.upload_pdf_qr_type_dropdown = page.locator("//button[@data-target='#acc_nameOfQrPdf']")
        self.upload_pdf_qr_type_button = page.locator("//div[@id='pdf']")
        self.upload_pdf_qr_type_drop_area = page.locator("#pdf")
        self.directly_show_pdf_checkbox = page.locator("//input[@id='direct_pdf']/following-sibling::label")
        self.add_pdf_information_qr_code_dropdown = page.locator("//button[@data-target='#acc_pdfInformation']")
        self.company_pdf_info_input = page.locator("//input[@id='company']")
        self.title_pdf_info_input = page.locator("//input[@id='pdftitle']")
        self.description_pdf_info_input = page.locator("//textarea[@id='description']")
        self.website_pdf_info_input = page.locator("//input[@id='website']")
        self.button_pdf_info_input = page.locator("//input[@id='button']")

        # Links QR code locators
        self.basic_info_links_qr_code_dropdown = page.locator("//button[@data-target='#acc_listInfo']")
        self.basic_info_links_qr_code_image_input = page.locator("//input[@id='companyLogo']")
<<<<<<< HEAD
=======
        #self.basic_info_links_qr_code_image_input = "//input[@id='companyLogo']"
        self.basic_info_company_logo_input = page.locator("//input[@id='companyLogo']")
>>>>>>> e61430e (commit before pull)
        self.basic_info_links_qr_code_title_input = page.locator("//input[@id='list_title']")
        self.basic_info_links_qr_code_description_input = page.locator("//textarea[@id='list_description']")
        self.list_of_links_qr_code_dropdown = page.locator("//button[@data-target='#acc_link']")
        self.list_of_links_qr_code_delete_button = page.locator("//div[@class='links-delete-wrap']/button")
        self.list_of_links_qr_code_image_input = page.locator("//input[@id='linkImages1']")
        self.list_of_links_qr_code_link_text_input = page.locator("//input[@id='list_text']")
        self.list_of_links_qr_code_link_url_input = page.locator("//input[@id='list_URL']")
        self.links_qr_code_social_network_url_input = page.locator("//input[@id='socialUrl']")
        self.links_qr_code_social_network_text_input = page.locator("//input[@name='social_icon_text[]']")

        # Vcard QR code locators
        self.v_card_qr_code_image_input = page.locator("//input[@id='companyLogo']")
        self.v_card_qr_code_first_name_input = page.locator("//input[@id='vcard_first_name']")
        self.v_card_qr_code_last_name_input = page.locator("//input[@id='vcard_last_name']")
        self.v_card_qr_code_company_details_dropdown = page.locator("//button[@data-target='#acc_companyInfo']")
        self.v_card_qr_code_company_details_company_input = page.locator("//input[@id='vcard_company']")
        self.v_card_qr_code_company_details_profession_input = page.locator("//input[@id='vcard_profession']")
        self.v_card_qr_code_company_details_summary_input = page.locator("//textarea[@id='vcard_note']")

        # Business QR code locators
        self.business_info_business_qr_type_image_input = page.locator("//input[@id='companyLogo']")
        self.business_info_business_qr_type_company_input = page.locator("//input[@id='company']")
        self.business_info_business_qr_type_title_input = page.locator("//input[@id='companyTitle']")
        self.business_info_business_qr_type_subtitle_input = page.locator("//input[@id='companySubtitle']")
        self.business_info_business_qr_type_add_button = page.locator("//button[@id='add']")
        self.about_company_business_qr_type_dropdown = page.locator("//textarea[@id='aboutCompany']")
        self.about_company_business_qr_type_textarea = page.locator("//textarea[@id='aboutCompany']")

        # Images QR code locators
        self.upload_image_qr_code_dropdown = page.locator("//button[@data-target='#acc_images']")
        self.upload_image_qr_code_button = page.locator("//div[@id='files']")
        self.upload_image_qr_code_drop_area = page.locator("#files")
        self.vertical_image_qr_code_checkbox = page.locator("//input[@id='uploadCheckbox']")
        self.image_information_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.image_information_qr_code_gallery_title_input = page.locator("//input[@id='image_title']")
        self.image_information_qr_code_gallery_description_input = page.locator("//textarea[@id='image_description']")
        self.image_information_qr_code_website_input = page.locator("//input[@id='website']")

        # Video QR code locators
        self.upload_video_qr_code_dropdown = page.locator("//button[@data-target='#acc_videoUpload']")
        self.upload_video_qr_code_url_input = page.locator("//input[@id='youTubeUrl']")
        self.upload_video_qr_code_button = page.locator("//div[@id='files']//button")
        self.upload_video_qr_code_drop_area = page.locator("#files")
        self.video_show_directly_qr_code_checkbox = page.locator("//input[@id='direct_video']")
        self.video_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_contactInfo']")
        self.video_info_qr_code_company_input = page.locator("//input[@id='companyName']")
        self.video_info_qr_code_video_title_input = page.locator("//input[@id='videoTitle']")
        self.video_info_qr_code_video_description_input = page.locator("//textarea[@id='videoDescription']")

        # Apps QR code locators
        self.app_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.app_info_qr_code_app_name_input = page.locator("//input[@id='app_title']")
        self.app_info_qr_code_dev_company_input = page.locator("//input[@id='app_company']")
        self.app_info_qr_code_logo_img_input = page.locator("//input[@id='companyLogo']")
        self.app_info_qr_code_description_input = page.locator("//textarea[@id='app_description']")
        self.app_info_qr_code_website_input = page.locator("//input[@id='app_website']")
        self.links_to_platforms_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.links_to_platforms_qr_code_google_add_button = page.locator("//button[contains(@class,'google_btn')]")
        self.links_to_platforms_qr_code_google_input = page.locator("//input[@id='google']")
        self.links_to_platforms_qr_code_apple_add_button = page.locator("//button[contains(@class,'apple_btn')]")
        self.links_to_platforms_qr_code_apple_input = page.locator("//input[@id='apple']")
        self.links_to_platforms_qr_code_amazon_add_button = page.locator("//button[contains(@class,'amazone_btn')]")
        self.links_to_platforms_qr_code_amazon_input = page.locator("//input[@id='amazon']")

        # Coupon QR code locators
        self.offer_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.offer_info_qr_code_img_input = page.locator("//input[@id='companyLogo']")
        self.offer_info_qr_code_company_input = page.locator("//input[@id='company']")
        self.offer_info_qr_code_title_input = page.locator("//input[@id='title']")
        self.offer_info_qr_code_description_input = page.locator("//textarea[@id='description']")
        self.offer_info_qr_code_badge_input = page.locator("//input[@id='salesBadge']")
        self.offer_info_qr_code_see_code_button = page.locator("//input[@id='buttonToSeeCode']")
        self.coupon_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_couponInfo']")
        self.coupon_info_qr_code_barcode_toggle = page.locator("//input[@id='couponTgl']")
        self.coupon_info_qr_code_code_input = page.locator("//input[@id='couponCode']")
        self.coupon_info_qr_code_terms_input = page.locator("//textarea[@id='terms']")
        self.coupon_info_qr_code_button_input = page.locator("//input[@id='buttonText']")
        self.coupon_info_qr_code_website_input = page.locator("//input[@id='buttonUrl']")

        # Mp3 QR code locators
        self.mp3_upload_dropdown = page.locator("//button[@data-target='#acc_nameOfMp3']")
        self.mp3_upload_add_option_checkbox = page.locator("//input[@id='addDownloadOption']")
        self.mp3_info_img_input = page.locator("//input[@id='companyLogo']")
        self.mp3_info_title_input = page.locator("//input[@id='mp3_title']")
        self.mp3_info_description_input = page.locator("//textarea[@id='mp3_description']")
        self.mp3_info_website_input = page.locator("//input[@id='mp3_website']")
        self.mp3_info_add_button = page.locator("//div[@id='btn-item']")
        self.mp3_info_button_text_input = page.locator("//input[@id='button_text']")
        self.mp3_info_button_website_input = page.locator("//input[@id='button_url']")
        self.mp3_info_button_remove_button = page.locator("//div[@id='add-btn']//button[contains(@class,'removeBtn')]")

        # Menu QR code locators
        self.menu_var_popup_modal_title = page.locator("//div[@id='helpCarousel1']//h5")
        self.menu_var_popup_menu_type_button = page.locator("//div[@id='menuModal']//button[@value='menu']")
        self.menu_var_popup_pdf_type_button = page.locator("//div[@id='menuModal']//button[@value='pdf']")
        self.menu_var_popup_web_type_button = page.locator("//div[@id='menuModal']//button[@value='url']")
        self.menu_var_popup_cross_button = page.locator("//div[@id='menuModal']//button[@value='url']")
        self.menu_menu_type_restaurant_dropdown = page.locator("//button[@data-target='#acc_menuInfo']")
        self.menu_menu_type_restaurant_img_input = page.locator("//input[@id='companyLogo']")
        self.menu_menu_type_restaurant_name_input = page.locator("//input[@id='companyTitle']")
        self.menu_menu_type_restaurant_description_input = page.locator("//textarea[@id='companyDescription']")
        self.menu_menu_type_menu_dropdown = page.locator("//button[@data-target='#acc_product']")
        self.menu_menu_type_section1_dropdown = page.locator(
            "//div[@id='add_section']//button[contains(@class,'section-btn') and @data-target='#menu_section_1']")
        self.menu_menu_type_section1_name_input = page.locator("//input[@id='sectionNames']")
        self.menu_menu_type_section1_description_of_section_input = page.locator("//input[@id='sectionDescriptions']")
        self.menu_menu_type_section1_image_input = page.locator("//input[@id='productImages1']")
        self.menu_menu_type_section1_product_name_input = page.locator(
            "//div[@class='row']//input[contains(@name,'productNames') and contains(@class,'pName')]")
        self.menu_menu_type_section1_name_translated_input = page.locator("//input[@id='productNamesTranslated']")
        self.menu_menu_type_section1_description_input = page.locator("//input[@id='productDescriptions']")
        self.menu_menu_type_section1_price_input = page.locator("//input[@id='productPrices']")
        # add allergens
        self.menu_link_type_url_input = page.locator("//input[@id='url']")

        # Wifi QR code locators
        self.wi_fi_info_dropdown = page.locator("//button[@data-target='#acc_WiFi_Information']")
        self.wi_fi_info_network_name_input = page.locator("//input[@id='wifi_ssid']")
        self.wi_fi_info_network_password_input = page.locator("//input[@id='wifi_password']")
        self.wi_fi_info_encrypting_type_dropdown = page.locator("//select[@id='wifi_encryption']")

        # Facebook QR code locators
        self.facebook_design_dropdown = page.locator("//button[@data-target='#facebook-bg']")
        self.facebook_design_image0 = page.locator("//div[@id='facebook-bg']//div[@data-image_id='0']")
        self.facebook_design_image1 = page.locator("//div[@id='facebook-bg']//div[@data-image_id='1']")
        self.facebook_design_image2 = page.locator("//div[@id='facebook-bg']//div[@data-image_id='2']")
        self.facebook_design_background_input = page.locator("//input[@id='fbBgImage']")
        self.facebook_profile_img_dropdown = page.locator("//button[@data-target='#facebook-profile']")
        self.facebook_profile_img_input = page.locator("//input[@id='companyLogo']")
        self.facebook_basic_info_dropdown = page.locator("//button[@data-target='#facebook-details']")
        self.facebook_basic_info_facebook_url = page.locator("//input[@id='facebook_url']")
        self.facebook_basic_info_facebook_title = page.locator("//input[@id='facebook_title']")
        self.facebook_basic_info_facebook_description = page.locator("//textarea[@id='facebook_description']")

        # Instagram QR code locators
        self.instagram_basic_info_dropdown = page.locator("//button[@data-target='#instagram_username']")
        self.instagram_basic_info_username_input = page.locator("//input[@id='inst_username']")

        # Social Media QR code locators
        self.social_media_design_dropdown = page.locator("//button[@data-target='#acc_Design']")
        self.social_media_basic_info_dropdown = page.locator("//button[@data-target='#social-media']")
        self.social_media_basic_info_title = page.locator("//input[@id='social_title']")
        self.social_media_basic_info_description = page.locator("//textarea[@id='social_description']")
        self.social_media_basic_info_description = page.locator("//textarea[@id='social_description']")

        # Whatsapp QR code locators
        self.whats_app_information_dropdown = page.locator("//button[@data-target='#whatsapp_no']")
        self.whats_app_information_phone_input = page.locator("//input[@id='phone']")
        self.whats_app_information_message_input = page.locator("//textarea[@id='whatsapp_body']")

        # Step 3 locators
        self.frame_step3_dropdown = page.locator("//button[@data-target='#acc_frame']")
        self.qrcode_patterns_step3_dropdown = page.locator("//button[@data-target='#acc_patterns']")
        self.qrcode_corners_step3_dropdown = page.locator("//button[@data-target='#acc_corners']")
        self.qrcode_add_logo_step3_dropdown = page.locator("//button[@data-target='#acc_addLogo']")
        self.qrcode_upload_logo_input = page.locator("//input[@id='qr_code_logo']")
        self.create_button = page.locator("//button[@id='temp_submit']")
        self.back_button = page.locator("//button[@id='cancel']")
        self.close_download_modal_button = page.locator("//div[@id='DownloadModal']//button[@aria-label='Close']")
        # Add QR design parameters Frame, QR code pattern, QR code corners, Add logo.

        # DPF Download locators

        # DPF QR code pricing
        self.days_14_limited_access_button = page.locator("//input[@id='dpfPlan1']")
        self.days_14_full_access_button = page.locator("//input[@id='dpfPlan2']")
        self.annual_plan_button = page.locator("//input[@id='dpfPlan3']")
        self.continue_user_plan_button = page.locator("//a[@id='user_plan_url']")

        # DPF Download locators
        self.dpf_form_title = page.locator("//form[@id='register-dpf-form']/div[@class='-form-title']")
        self.dpf_form_email_input = page.locator("//input[@id='input-email']")
        self.dpf_form_submit_button = page.locator("//button[contains(@class,'-btn-submit')]")

        # DPF Congratulations modal window
        self.congrats_title_h2 = page.locator("//div[@class='thank-you']/h2")
        self.congrats_download_button = page.locator("//div[@class='thank-you']/div[@class='thank-btn-area']/a")
