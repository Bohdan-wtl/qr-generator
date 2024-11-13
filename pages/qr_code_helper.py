import random
import os
import time
from pathlib import Path

import allure
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
from faker import Faker
from pydub.generators import Sine
from moviepy.editor import ColorClip


class QrCodeHelper:
    def __init__(self, page, locator):
        self.page = page
        self.locator = locator
        self.faker = Faker()
        self.generated_files_dir = Path(os.getcwd()) / "generated_files"
        self.generated_files_dir.mkdir(parents=True, exist_ok=True)
        self.screenshot_path = None

    @allure.step("Generate file")
    def generate_file(self, file_type):
        timestamp = int(time.time())
        file_path = self.generated_files_dir

        if file_type == 'image':
            image_filename = f"generated_image_{timestamp}.jpg"
            image_path = file_path / image_filename
            image = Image.new('RGB', (2440, 2440), color=(000, 111, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            text = f"{self.faker.texts(max_nb_chars=5000)} {timestamp}"
            draw.text((10, 10), text, font=font, fill=(0, 0, 0))
            image.save(image_path, format="JPEG", quality=95)
            return image_path

        elif file_type == 'mp4':
            mp4_filename = f"generated_file_{timestamp}.mp4"
            mp4_path = file_path / mp4_filename
            duration = 5
            fps = 24
            color = (0, 0, 255)
            resolution = (640, 480)
            clip = ColorClip(size=resolution, color=color, duration=duration)
            clip = clip.set_fps(fps)
            clip.write_videofile(str(mp4_path), codec="libx264", fps=fps)
            return mp4_path

        elif file_type == 'pdf':
            pdf_filename = f"generated_file_{timestamp}.pdf"
            pdf_path = file_path / pdf_filename
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(190, 10, txt=f"{self.faker.texts(max_nb_chars=5000)} {timestamp}", align='C')
            pdf.output(pdf_path)
            return pdf_path

        elif file_type == 'mp3':
            mp3_filename = f"generated_file_{timestamp}.mp3"
            mp3_path = file_path / mp3_filename
            sine_wave = Sine(340)
            audio = sine_wave.to_audio_segment(duration=5000)
            audio.export(mp3_path, format='mp3')
            return mp3_path

    @allure.step("Emulate drag and drop")
    def emulate_drag_and_drop(self, selector, file_type):
        file_path = self.generate_file(file_type)
        mime_type_mapping = {
            '.pdf': 'application/pdf',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.mp3': 'audio/mpeg',
            '.mp4': 'video/mp4',
            '.avi': 'video/x-msvideo',
        }
        file_extension = file_path.suffix.lower()
        mime_type = mime_type_mapping.get(file_extension, 'application/octet-stream')
        with open(file_path, 'rb') as file:
            file_content = file.read()
        self.page.evaluate("""
          (data) => {
            const { fileContent, selector, mimeType, fileName } = data;
            const dropArea = document.querySelector(selector);
            const dataTransfer = new DataTransfer();
            const file = new File([new Uint8Array(fileContent)], fileName, { type: mimeType });

            dataTransfer.items.add(file);
            dropArea.dispatchEvent(new DragEvent('dragenter', { dataTransfer }));
            dropArea.dispatchEvent(new DragEvent('drop', { dataTransfer }));
          }
        """, {
            'fileContent': list(file_content),
            'selector': selector,
            'mimeType': mime_type,
            'fileName': file_path.name
        })

    @allure.step("Set file")
    def set_file(self, selector, file_type):
        file_path = self.generate_file(file_type)
        selector.set_input_files(file_path)

    @allure.step("Close help modal window step 3")
    def close_help_modal_window_st3(self):
        self.locator.help_modal_close_button.is_visible()
        self.locator.help_modal_close_button.click()

    @allure.step("Close help modal window step 2")
    def close_help_modal_window_st2(self):
        self.locator.help_modal_close_button.wait_for(state="visible")
        self.locator.help_modal_close_button.is_enabled()
        self.locator.help_modal_close_button.click()
        self.page.wait_for_selector(self.locator.modal_window_step2, state="hidden", timeout=5000)

    @allure.step("Set QR code name")
    def set_custom_qr_code_name(self, qr_code_type):
        self.locator.custom_name_qr_code_dropdown.click()
        custom_qr_code_name = self.locator.custom_name_qr_code_input.fill(
            f"{qr_code_type}_{str(self.faker.random_number(digits=9, fix_len=True))}")
        return custom_qr_code_name

    @allure.step("Set QR code style")
    def fonts_style_select(self):
        self.locator.update_fonts_qr_code_dropdown.click()
        self.locator.fonts_title_dropdown.scroll_into_view_if_needed()
        self.locator.fonts_title_dropdown.click(force=True)
        self.page.wait_for_selector("//div[@id='dropdown_title']/button", state="attached")
        title_options = self.page.query_selector_all("//div[@id='dropdown_title']/button")
        random_title_font = random.choice(title_options)
        random_title_font.scroll_into_view_if_needed()
        random_title_font.click(force=True)
        self.page.wait_for_timeout(1000)
        self.locator.fonts_texts_dropdown.click()
        text_options = self.page.query_selector_all("//div[@id='dropdown_text']/button")
        random_text_font = random.choice(text_options)
        random_text_font.scroll_into_view_if_needed()
        random_text_font.click(force=True)
        random_text_font.click(force=True)

    @allure.step("Set QR code image on welcome screen")
    def welcome_screen_set_img(self):
        image_path = self.generate_file('image')
        self.locator.upload_welcome_screen_qr_code_dropdown.click()
        self.locator.upload_welcome_screen_qr_code_input.set_input_files(image_path)

    @allure.step("Select random option")
    def select_random_option(self, locators):
        random_locator = random.choice(locators)
        self.page.locator(random_locator).click()
        return random_locator

    @allure.step("Select qr frame on step 3")
    def select_frame_step3(self):
        self.locator.frame_step3_dropdown.is_enabled()
        self.locator.frame_step3_dropdown.click()
        self.select_random_child_by_attribute("#acc_frame .frameWrapper", "button", "id")

    @allure.step("Select QR cornets on step 3")
    def select_qrcode_corners_step3(self):
        self.select_random_child_by_attribute(
            "//div[@id='acc_corners']//div[@class='col-md-6']//div[@class='cornerBtn-container']", 'label', 'id')
        self.select_random_child_by_attribute(
            "//div[@id='acc_corners']//div[contains(@class,'col-md-5')]//div[@class='cornerBtn-container']", 'label',
            'id')

    @allure.step("Add phone, email and website")
    def add_phone_email_website(self):
        self.locator.contact_details_qr_code_add_phone_btn.scroll_into_view_if_needed()
        self.locator.contact_details_qr_code_add_phone_btn.click()
        self.locator.contact_details_qr_code_add_phone_label.fill(self.faker.word())
        self.locator.contact_details_qr_code_add_phone_number.fill(self.faker.basic_phone_number())
        self.locator.contact_details_qr_code_add_email_btn.scroll_into_view_if_needed()
        self.locator.contact_details_qr_code_add_email_btn.click()
        self.locator.contact_details_qr_code_add_email_label.fill(self.faker.word())
        self.locator.contact_details_qr_code_add_email_address.fill(self.faker.email())
        self.locator.contact_details_qr_code_add_website_btn.scroll_into_view_if_needed()
        self.locator.contact_details_qr_code_add_website_btn.click()
        self.locator.contact_details_qr_code_add_website_label.fill(self.faker.word())
        self.locator.contact_details_qr_code_add_website_url.fill(self.faker.url())

    @allure.step("Set location")
    def set_location(self):
        self.locator.location_qr_code_search_address.click()
        self.locator.location_qr_code_search_address.fill(self.faker.city())
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

    def select_random_child_by_attribute(self, parent_selector, child_tag, unique_attribute):
        parent_element = self.page.query_selector(parent_selector)
        if not parent_element:
            return
        child_elements = parent_element.query_selector_all(f"{child_tag}[{unique_attribute}]")
        if not child_elements:
            return
        attribute_values = [child.get_attribute(unique_attribute) for child in child_elements if
                            child.get_attribute(unique_attribute)]
        if not attribute_values:
            return
        random_value = random.choice(attribute_values)
        for child in child_elements:
            if child.get_attribute(unique_attribute) == random_value:
                child.scroll_into_view_if_needed()
                child.click()
                break

    @allure.step("Set path for screenshot")
    def set_screenshot_path(self, screenshot_path):
        self.screenshot_path = screenshot_path

    @allure.step("Take iframe screenshot on step 2")
    def take_iframe_screenshot(self):
        self.page.add_style_tag(content="""
        .card {
            border-radius: 0px !important;
        }
        .mb-frame-inner .card {
            max-width: none !important;
        }
        .mb-frame-inner .card::after {
            background-image: none !important;
        }
        #iframesrc, #iframesrc * {
            border-radius: 0px !important;
        }
        .mb-frame {
            padding: 0px !important;
        }
        .App {
            overflow: visible !important;
            height: auto !important;
        }
    """)
        footer_element = self.page.locator("//div[@id='qr-proceed-footer']")
        footer_element.evaluate("element => element.style.display = 'none'")
        self.page.locator("//div[@id='preview_qrcode']").evaluate("element => element.style.display = 'none'")
        self.page.locator("//header").evaluate("element => element.style.display = 'none'")
        self.page.locator("//div[@class='iphone-line']").evaluate("element => element.style.display = 'none'")
        mobile = self.page.locator("//div[@id='tabs-1']/div")
        mobile.evaluate("element => element.style.overflow = 'visible'")
        mobile.evaluate("element => element.style.backgroundImage = 'none'")
        iframe = self.page.frame_locator("iframe#iframesrc").locator("//div[@class='App']")
        iframe.evaluate("element => element.style.background = 'white'")
        iframe_height = (self.page.frame_locator("iframe#iframesrc")
                         .locator("//div[@class='App']")
                         .evaluate("element => element.scrollHeight"))
        self.page.frame_locator("iframe#iframesrc").locator("//html/head").evaluate("""
            () => {
                window.scrollTo({ top: 0, behavior: "smooth" });
            }
        """)
        mobile.evaluate(f"element => element.style.height = '{iframe_height}px'")
        iframe.screenshot(path=str(self.screenshot_path))
        footer_element.evaluate("element => element.style.display = 'block'")

    def preview_loader_active_and_not_active_state(self):
        self.page.wait_for_function(
            "document.querySelector('#loader') && document.querySelector('#loader').classList.contains('active')")
        self.page.wait_for_function(
            "document.querySelector('#loader') && !document.querySelector('#loader').classList.contains('active')")