
class AdminPage:

    def __init__(self, page):

        # Admin Log In page
        self.page = page
        self.user_email = None
        self.admin_email_input = page.locator("//input[@id='input-email']")
        self.admin_password_input = page.locator("//input[@id='input-password']")
        self.admin_log_in_button = page.locator("//button[@id='login-btn']")

        # Admin left menu
        self.menu_dashboard_button = page.locator("//a[.//span[contains(text(),'Dashboard')]]")
        self.menu_users_button = page.locator("//a[.//span[contains(text(),'Users')]]")
        self.menu_qr_codes_button = page.locator("//a[.//span[text()='QR codes']]")
        self.menu_archived_qr_codes_button = page.locator("//a[.//span[contains(text(),'Archived')]]")
        self.menu_payments_button = page.locator("//a[.//span[contains(text(),'Payments')]]")

        # Admin Users page
        self.global_search_input = page.locator("//input[@id='global_search']")
        self.search_button = page.locator("//button[contains(text(),'Search')]")

        # User menu dropdown
        self.generate_discount_url_btn = page.locator("//div[contains(@class,'dropdown-menu')]/a[text()=' Generate URL']")

        # Link discount variables pop up
        self.pricing_popup_close_button = page.locator("//div[@id='user_plan_generate_modal']//button[@class='close']")
        self.default_pricing_button = page.locator("//h5[contains(text(),'Default Pricing Page')]")
        self.discount_70_promo_button = page.locator("//h5[contains(text(),'70% OFF Promo Page')]")
        self.discount_8_99_monthly_button = page.locator("//h5[contains(text(),'$8.99 Monthly Page')]")
        self.discount_50_one_time_button = page.locator("//h5[contains(text(),'$50 One Time Payment Page')]")
        self.create_new_password_button = page.locator("//h5[contains(text(),'Create New Password')]")
        self.generate_link_button = page.locator("//a[@id='user_payment_url']")
        self.generated_link = page.locator("//div[contains(@class,'url-view-block active')]")

        # Refund form
        self.full_refund_plan_button_cancel_subscription = page.locator("//label[.//input[@id='option1']]")
        self.full_refund_plan_button_keep_subscription = page.locator("//label[.//input[@id='option2']]")
        self.partial_refund_plan_button_cancel_subscription = page.locator("//label[.//input[@id='option3']]")
        self.partial_refund_plan_button_keep_subscription = page.locator("//label[.//input[@id='option4']]")
        self.refund_confirm_button_payments_tab = page.locator("//button[@id='refund_btn']")
        self.refund_alert_message = page.locator("//div[button[@data-dismiss='alert']]")
        self.refund_amount_input_field = page.locator("//input[@id='refund_amount']")
        self.refund_amount_input_payment_button = page.locator("//button[@id='partial_refund_btn']")

        # Log out button
        self.admin_logout_area = page.locator("//ul[2]/li/a")
        self.admin_logout_button = page.locator("//ul[2]/li/div/a")

    def get_user_menu_dots_button_users_tab(self, user_email):
        return self.page.locator(f"//tr[td//a[contains(text(), '{user_email}')]]//div[contains(@class, 'dropdown')]//button")

    def get_user_menu_dots_button_payments_tab(self, email_dpf):
        return self.page.locator(f"//tr[.//span[contains(text(),'{email_dpf}')]]//div[contains(@class,'dropdown actions-dropdown')]")

    def get_user_menu_refund_button_payments_tab(self, email_dpf):
        return self.page.locator(f"//tr[.//span[contains(text(),'{email_dpf}')]]//a[text()=' Refund']")