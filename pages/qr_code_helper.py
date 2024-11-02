import random
import os
import time
from pathlib import Path
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

    def generate_file(self, file_type):
        timestamp = int(time.time())
        file_path = self.generated_files_dir

        if file_type == 'image':
            image_filename = f"generated_image_{timestamp}.png"
            image_path = file_path / image_filename
            image = Image.new('RGB', (800, 600), color=(0, 111, 255))
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            text = f"{self.faker.text(max_nb_chars=500)} {timestamp}"
            draw.text((10, 10), text, font=font, fill=(0, 0, 0))
            image.save(image_path)
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
            pdf.multi_cell(190, 10, txt=f"{self.faker.text(max_nb_chars=5000)} {timestamp}", align='C')
            pdf.output(str(pdf_path))
            return pdf_path

        elif file_type == 'mp3':
            mp3_filename = f"generated_file_{timestamp}.mp3"
            mp3_path = file_path / mp3_filename
            sine_wave = Sine(340)
            audio = sine_wave.to_audio_segment(duration=5000)
            audio.export(mp3_path, format='mp3')
            return mp3_path

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
        self.page.wait_for_selector("//span[@class='image-edit-icon']", state="visible")

    def set_file(self, selector, file_type):
        file_path = self.generate_file(file_type)
        self.page.locator(selector).set_input_files(file_path)

    def close_help_modal_window_st3(self):
        if self.locator.help_modal_close_button.is_visible():
            self.locator.help_modal_close_button.click()
        else:
            pass

    def close_help_modal_window_st2(self):
        if self.locator.help_modal_close_button.is_visible():
            self.locator.help_modal_close_button.click()
            self.page.wait_for_selector(self.locator.modal_window_step2, state="hidden", timeout=5000)
        else:
            pass

    def wait_for_loader_disappear(self):
        if self.locator.loader_img.is_visible():
            self.page.wait_for_selector(self.locator.loader_img, state="hidden")
        else:
            pass

    def select_random_colors(self):
        design_color_style_locators = [
            "//div[@id='formcolorPalette1']",
            "//div[@id='formcolorPalette2']",
            "//div[@id='formcolorPalette4']",
            "//div[@id='formcolorPalette5']",
            "//div[@id='formcolorPalette6']",
            "//div[@id='formcolorPalette7']"
        ]
        random_design = random.choice(design_color_style_locators)
        self.page.locator(random_design).click()
        return random_design

    def set_custom_qr_code_name(self, qr_code_type):
        self.locator.custom_name_qr_code_dropdown.click()
        custom_qr_code_name = self.locator.custom_name_qr_code_input.fill(
            f"{qr_code_type}_{str(self.faker.random_number(digits=9, fix_len=True))}")
        return custom_qr_code_name

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

    def welcome_screen_set_img(self):
        image_path = self.generate_file('image')
        self.locator.upload_welcome_screen_qr_code_dropdown.click()
        self.page.locator(self.locator.upload_welcome_screen_qr_code_input).set_input_files(image_path)

    def select_random_option(self, locators):
        random_locator = random.choice(locators)
        self.page.locator(random_locator).click()
        return random_locator

    def select_frame_step3(self):
        self.locator.frame_step3_dropdown.click()
        frame_locators = [
            "//button[@id='qr_frame_id_{}']".format(i) for i in range(16)
        ]
        return self.select_random_option(frame_locators)

    def select_pattern_step3(self):
        self.locator.qrcode_patterns_step3_dropdown.click()
        pattern_locators = [
            "//label[@id='square']", "//label[@id='round']", "//label[@id='extra_rounded']",
            "//label[@id='dot']", "//label[@id='heart']", "//label[@id='diamond']"
        ]
        return self.select_random_option(pattern_locators)

    def select_qrcode_corners_step3(self):
        self.locator.qrcode_corners_step3_dropdown.click()
        self.select_random_option([
            "//label[@id='NS']", "//label[@id='FR']", "//label[@id='FS']",
            "//label[@id='FRR']", "//label[@id='FF']", "//label[@id='FL']"
        ])
        self.select_random_option([
            "//label[@id='IN']", "//label[@id='ID']", "//label[@id='IS']",
            "//label[@id='IR']", "//label[@id='IDD']", "//label[@id='IF']", "//label[@id='IL']"
        ])

    def select_random_social_network_option(self):
        social_networks_locators = [
            "//button[@id='socialicon_id_web']", "//button[@id='socialicon_id_dribbble']",
            "//button[@id='socialicon_id_facebook']", "//button[@id='socialicon_id_flickr']",
            "//button[@id='socialicon_id_gitHub']", "//button[@id='socialicon_id_GitLab']",
            "//button[@id='socialicon_id_Google Review']", "//button[@id='socialicon_id_line']",
            "//button[@id='socialicon_id_linkedIn']", "//button[@id='socialicon_id_pinterest']",
            "//button[@id='socialicon_id_reddit']", "//button[@id='socialicon_id_skype']",
            "//button[@id='socialicon_id_snapchat']", "//button[@id='socialicon_id_tripAdvisor']",
            "//button[@id='socialicon_id_tumblr']", "//button[@id='socialicon_id_X']",
            "//button[@id='socialicon_id_vimeo']", "//button[@id='socialicon_id_vkontakte']",
            "//button[@id='socialicon_id_xing']", "//button[@id='socialicon_id_YouTube']",
            "//button[@id='socialicon_id_instagram']", "//button[@id='socialicon_id_TikTok']",
            "//button[@id='socialicon_id_WhatsApp']", "//button[@id='socialicon_id_telegram']",
            "//button[@id='socialicon_id_Facebook Messenger']", "//button[@id='socialicon_id_yelp']",
            "//button[@id='socialicon_id_Uber Eats']", "//button[@id='socialicon_id_postmates']",
            "//button[@id='socialicon_id_OpenTable']", "//button[@id='socialicon_id_spotify']",
            "//button[@id='socialicon_id_SoundCloud']", "//button[@id='socialicon_id_Apple Music']",
            "//button[@id='socialicon_id_OnlyFans']", "//button[@id='socialicon_id_DoorDash']",
            "//button[@id='socialicon_id_trustpilot']", "//button[@id='socialicon_id_signal']",
            "//button[@id='socialicon_id_WeChat']"
        ]
        return self.select_random_option(social_networks_locators)

    def set_screenshot_path(self, screenshot_path):
        self.screenshot_path = screenshot_path

    def take_iframe_screenshot(self):
        self.page.add_style_tag(content="""
        .card {
            border-radius: 0px !important;
            width: 430px !important;
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
        """)
        footer_element = self.page.locator("//div[@id='qr-proceed-footer']")
        footer_element.evaluate("element => element.style.display = 'none'")
        mobile = self.page.locator("//div[@id='tabs-1']/div")
        iphone_line = self.page.locator("//div[@class='iphone-line']")
        iphone_line.evaluate("element => element.style.position = 'none'")
        mobile.evaluate("element => element.style.height = '100vh'")
        mobile.evaluate("element => element.style.backgroundImage = 'none'")
        iframe = self.page.frame_locator("//iframe[@id='iframesrc']")
        iframe.locator("//div[@class='App']").screenshot(path=str(self.screenshot_path))
        footer_element.evaluate("element => element.style.display = ''")
