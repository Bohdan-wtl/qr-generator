from dotenv import load_dotenv
import os


def get_env(var):
    load_dotenv()
    return os.getenv(var)


languages = ['en'
             #    "ar",
             #    "bg",
             #    "cs", "da", "de", "en",
             #      "bg", "cs", "da", "de", "el", "es", "fi", "fr", "he", "hi", "hr", "hu", "id",
             #      "it", "ja", "ko", "ms", "nl", "no", "pl", "pt", "pt-br", "ro", "sk", "sl", "sr", "sv",
             #      "th", "tr", "uk", "zh-cn", "zh-hk"
             ]

qr_create_methods = [
    "wifi_qr_create",
    "instagram_qr_create", "mp3_qr_create", "coupon_qr_create",
    "menu_menu_qr_create", "facebook_qr_create", "apps_qr_create", "links_qr_create",
    "menu_pdf_qr_create", "pdf_qr_create", "social_media_qr_create", "whatsapp_qr_create",
    "video_qr_create", "image_qr_create", "business_qr_create", "vcard_qr_create"
]

resolution_qr_code_images = [
    "Default", "512x512", "1024x1024", "2048x2048", "4096x4096"
]
resolution_qr_code_pdf = [
    "Default", "A4", "A3", "A2", "A1", "A0"
]
eps_download_format = "EPS"
jpeg_download_format = "JPEG"
pdf_download_format = "PDF"
png_download_format = "PNG"
svg_download_format = "SVG"

download_params_default_modal = [
    {"file_format": "EPS", "resolution": "Default"},
    {"file_format": "EPS", "resolution": "512x512"},
    {"file_format": "EPS", "resolution": "1024x1024"},
    {"file_format": "EPS", "resolution": "2048x2048"},
    {"file_format": "EPS", "resolution": "4096x4096"},
    {"file_format": "PDF", "resolution": "Default"},
    {"file_format": "PDF", "resolution": "A4"},
    {"file_format": "PDF", "resolution": "A3"},
    {"file_format": "PDF", "resolution": "A2"},
    {"file_format": "PDF", "resolution": "A1"},
    {"file_format": "PDF", "resolution": "A0"},
    {"file_format": "JPEG", "resolution": "Default"},
    {"file_format": "JPEG", "resolution": "512x512"},
    {"file_format": "JPEG", "resolution": "1024x1024"},
    {"file_format": "JPEG", "resolution": "2048x2048"},
    {"file_format": "JPEG", "resolution": "4096x4096"},
    {"file_format": "PNG", "resolution": "Default"},
    {"file_format": "PNG", "resolution": "512x512"},
    {"file_format": "PNG", "resolution": "1024x1024"},
    {"file_format": "PNG", "resolution": "2048x2048"},
    {"file_format": "PNG", "resolution": "4096x4096"},
    {"file_format": "SVG", "resolution": "Default"},
    {"file_format": "SVG", "resolution": "512x512"},
    {"file_format": "SVG", "resolution": "1024x1024"},
    {"file_format": "SVG", "resolution": "2048x2048"},
    {"file_format": "SVG", "resolution": "4096x4096"},
]
