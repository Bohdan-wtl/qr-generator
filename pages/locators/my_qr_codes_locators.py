from base.base_page import BasePage


class MyQrCodesLocators:
    def __init__(self, page):
        self.page = page
        self.base = BasePage(page)
        self.download_modal_h3_title = self.base.locator("//div[@id='DownloadModal']//h3")
        self.download_modal_close_button = self.base.locator("//div[@id='DownloadModal']//button[@type='button']")
        self.download_qr_code_button = self.base.locator(
            "//div[contains(@class,'position-relative')]/button[@data-target='#DownloadModal']")
        self.download_button = self.base.locator("//div[@class='dl-modal-footer-buttons']/button")
        self.png_file_download = self.base.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='PNG']")
        self.jpeg_file_download = self.base.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='JPEG']")
        self.svg_file_download = self.base.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='SVG']")
        self.pdf_file_download = self.base.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='PDF']")
        self.eps_file_download = self.base.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='EPS']")
        self.print_file_download = self.base.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='Print']")
        self.size_of_qr_file_download_dropdown = self.base.locator(
            "//div[contains(@class,'dl-modal-size-picker')]/span[contains(@class,'icon-arrow-down')]")
        self.size_default_of_qr_file_download = self.base.locator("//input[@id='Default']")
        self.size_512_of_qr_file_download = self.base.locator("//input[@id='512x512']")
        self.size_1024_of_qr_file_download = self.base.locator("//input[@id='1024x1024']")
        self.size_2048_of_qr_file_download = self.base.locator("//input[@id='2048x2048']")
        self.size_4096_of_qr_file_download = self.base.locator("//input[@id='4096x4096']")
        self.sign_up_success_image = self.base.locator("//img[contains(@class,'dl-modal-head-img')]")
        self.create_qr_code_button = self.base.locator("//button[@data-target='#CreateQrCodeModal']")
        self.header_create_qr_code_button = self.base.locator("(//div[contains(@class, 'content-end')]/div)[2]")
