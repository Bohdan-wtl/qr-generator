from dotenv import load_dotenv
import os

def get_env(var):
    load_dotenv()
    return os.getenv(var)

languages = [
    "ar",
    #"bg", "cs", "da", "de", "el", "en", "es", "fi", "fr", "he", "hi", "hr", "hu", "id",
    # "it", "ja", "ko", "ms", "nl", "no", "pl", "pt", "pt-br", "ro", "sk", "sl", "sr", "sv",
    # "th", "tr", "uk", "zh-cn", "zh-hk"
]

qr_create_methods = [
    "wifi_qr_create",
    "instagram_qr_create", "mp3_qr_create", "coupon_qr_create",
    "menu_menu_qr_create", "facebook_qr_create", "apps_qr_create", "links_qr_create",
    "menu_pdf_qr_create", "pdf_qr_create", "social_media_qr_create", "whatsapp_qr_create",
    "video_qr_create", "image_qr_create", "business_qr_create", "vcard_qr_create"
]

