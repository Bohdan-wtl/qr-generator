class MyQrCodesLocators:
    def __init__(self, page):
        self.download_modal_h3_title = page.locator("//div[@id='DownloadModal']//h3")
        self.download_modal_close_button = page.locator("//div[@id='DownloadModal']//button[@type='button']")
        self.download_qr_code_button = page.locator(
            "//div[contains(@class,'position-relative')]/button[@data-target='#DownloadModal']")
        self.download_button = page.locator("//div[@class='dl-modal-footer-buttons']/button")
        self.alert_locator = page.locator("//div[@id='alert_msg']")
        self.png_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='PNG']")
        self.jpeg_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='JPEG']")
        self.svg_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='SVG']")
        self.pdf_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='PDF']")
        self.eps_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='EPS']")
        self.print_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='Print']")
        self.size_of_qr_file_download_dropdown = page.locator(
            "//div[contains(@class,'dl-modal-size-picker')]/span[contains(@class,'icon-arrow-down')]")
        self.size_default_of_qr_file_download = page.locator("//input[@id='Default']")
        self.size_512_of_qr_file_download = page.locator("//input[@id='512x512']")
        self.size_1024_of_qr_file_download = page.locator("//input[@id='1024x1024']")
        self.size_2048_of_qr_file_download = page.locator("//input[@id='2048x2048']")
        self.size_4096_of_qr_file_download = page.locator("//input[@id='4096x4096']")
        self.sign_up_success_image = page.locator("//img[contains(@class,'dl-modal-head-img')]")
        self.create_qr_code_button = page.locator("//button[@data-target='#CreateQrCodeModal']")
        self.header_create_qr_code_button = page.locator("(//div[contains(@class, 'content-end')]/div)[2]")
