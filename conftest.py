import os
import allure
import pytest
import requests
from pytest import hookimpl
from playwright.sync_api import sync_playwright
from random import Random

headless = True

DELETE_USER_URL = "https://oqg-staging.test-qr.com/api/test-user-delete"

@pytest.fixture(scope="session")
@allure.title(f"Set up browser: {os.getenv('BROWSER')}")
def browser(request):
    with sync_playwright() as p:
        browser_type = os.getenv("BROWSER", "chromium")
        browser = getattr(p, browser_type).launch(headless=headless)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(request, browser):
    context = browser.new_context(viewport={"width": 1440, "height": 1080}, record_video_dir="artifacts/videos/")
    #context.tracing.start(name=f"{request.node.name}.zip",screenshots=True, snapshots=True)
    yield context
    #context.tracing.stop(path=f"traces/{request.node.name}.zip")
    context.close()

@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"artifacts/screenshots/{request.node.name}.png", full_page=True)
    page.close()
    if request.node.rep_call.failed:
        page.video.save_as(path=f"artifacts/videos/{request.node.name}.webm")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
@allure.title("Failed test artifacts")
def artifacts(request):
    yield
    if request.node.rep_call.failed:
        allure.attach.file(f"artifacts/screenshots/{request.node.name}.png", name="screenshot",
                           attachment_type=allure.attachment_type.PNG)
        allure.attach.file(f"artifacts/videos/{request.node.name}.webm", name="video",
                           attachment_type=allure.attachment_type.WEBM)
        #allure.attach.file(f"traces/{request.node.name}.zip", name="trace",
        #                   attachment_type="application/zip")


@pytest.fixture(scope='function')
def fake_email():
    random_number = Random().randint(3000, 9999999999999)
    fake_email = f"wtl-automation{random_number}@test.com"
    return fake_email


@pytest.fixture(scope='function')
@allure.title("Sign up")
def sign_up_fixture(request, fake_email, language):
    base_url = f"https://oqg-staging.test-qr.com/{language}/"
    email = fake_email
    request.instance.main_page.open_page(f"{base_url}register/")
    request.instance.register_page.sign_up(email, email)
    yield

@pytest.fixture(scope='function')
@allure.title("Navigate to DPF funnel")
def navigate_to_dpf_page(request, language):
    base_url = f"https://oqg-staging.test-qr.com/{language}/create?step=1&qr_onboarding=active_dpf"
    request.instance.main_page.open_page(base_url)

@pytest.fixture(scope='function')
@allure.title("Navigate to NSF funnel")
def navigate_to_nsf_page(request, language):
    base_url = f"https://oqg-staging.test-qr.com/{language}/create?step=1&qr_onboarding=active_nsf"
    request.instance.main_page.open_page(base_url)

@pytest.fixture(scope='function', autouse=True)
@allure.title("Delete user after test")
def delete_user_after_test(fake_email):
    yield
    headers = {"Content-Type": "application/json"}
    data = {
        "emails": [fake_email]
    }
    response = requests.post(DELETE_USER_URL, headers=headers, json=data)
    if response.status_code == 200:
        pass
    else:
        print(f"Failed to delete user with email {fake_email}. Status code: {response.status_code}")
