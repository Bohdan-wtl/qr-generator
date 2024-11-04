from dotenv import load_dotenv
import os

def get_env(var):
    load_dotenv()
    return os.getenv(var)


languages_urls = {
    "en": "https://oqg-staging.test-qr.com/en",
    #"ar": "https://oqg-staging.test-qr.com/ar",
}

languages_dpf_urls = {
    "en": "https://oqg-staging.test-qr.com/create?step=1&qr_onboarding=active_dpf",
    #"bg": "https://oqg-staging.test-qr.com/bg/create?step=1&qr_onboarding=active_dpf"
}

languages_nsf_urls = {
    "en": "https://oqg-staging.test-qr.com/create?step=1&qr_onboarding=active_nsf",
    #"zh-hk": "https://oqg-staging.test-qr.com/zh-hk/create?step=1&qr_onboarding=active_nsf"
}