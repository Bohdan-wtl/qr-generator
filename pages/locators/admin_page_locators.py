from base.base_page import BasePage


class AdminPageLocators:

    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        # Admin Log In page
        self.user_email = None
        self.admin_email_input = self.base.locator("//input[@id='input-email']")
        self.admin_password_input = self.base.locator("//input[@id='input-password']")
        self.admin_log_in_button = self.base.locator("//button[@id='login-btn']")

        # Admin left menu
        self.menu_dashboard_button = self.base.locator("//a[.//span[contains(text(),'Dashboard')]]")
        self.menu_users_button = self.base.locator("//a[.//span[contains(text(),'Users')]]")
        self.menu_qr_codes_button = self.base.locator("//a[.//span[text()='QR codes']]")
        self.menu_archived_qr_codes_button = self.base.locator("//a[.//span[contains(text(),'Archived')]]")
        self.menu_payments_button = self.base.locator("//a[.//span[contains(text(),'Payments')]]")

        # Admin Users page
        self.global_search_input = self.base.locator("//input[@id='global_search']")
        self.search_button = self.base.locator("//button[contains(text(),'Search')]")

        # User menu dropdown
        self.generate_discount_url_btn = self.base.locator(
            "//div[contains(@class,'dropdown-menu')]/a[text()=' Generate URL']")

        # Link discount variables pop up
        self.pricing_popup_close_button = self.base.locator("//div[@id='user_plan_generate_modal']//button[@class='close']")
        self.default_pricing_button = self.base.locator("//h5[contains(text(),'Default Pricing Page')]")
        self.discount_70_promo_button = self.base.locator("//h5[contains(text(),'70% OFF Promo Page')]")
        self.discount_8_99_monthly_button = self.base.locator("//h5[contains(text(),'$8.99 Monthly Page')]")
        self.discount_50_one_time_button = self.base.locator("//h5[contains(text(),'$50 One Time Payment Page')]")
        self.create_new_password_button = self.base.locator("//h5[contains(text(),'Create New Password')]")
        self.generate_link_button = self.base.locator("//a[@id='user_payment_url']")
        self.generated_link = self.base.locator("//div[contains(@class,'url-view-block active')]")

        # Refund form
        self.full_refund_plan_button_cancel_subscription = self.base.locator("//label[.//input[@id='option1']]")
        self.full_refund_plan_button_keep_subscription = self.base.locator("//label[.//input[@id='option2']]")
        self.partial_refund_plan_button_cancel_subscription = self.base.locator("//label[.//input[@id='option3']]")
        self.partial_refund_plan_button_keep_subscription = self.base.locator("//label[.//input[@id='option4']]")
        self.refund_confirm_button_payments_tab = self.base.locator("//button[@id='refund_btn']")
        self.refund_alert_message = self.base.locator("//div[button[@data-dismiss='alert']]")
        self.refund_amount_input_field = self.base.locator("//input[@id='refund_amount']")
        self.refund_amount_input_payment_button = self.base.locator("//button[@id='partial_refund_btn']")

        # Log out button
        self.admin_logout_area = self.base.locator("//ul[2]/li/a")
        self.admin_logout_button = self.base.locator("//ul[2]/li/div/a")
