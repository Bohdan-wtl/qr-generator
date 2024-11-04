import os
import shutil
import allure
import pytest
from pytest import hookimpl
from playwright.sync_api import sync_playwright

headless = False


@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(request, browser):
    context = browser.new_context(viewport={"width": 1440, "height": 1080}, record_video_dir="videos/")
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    page.close()
    if request.node.rep_call.failed:
        page.video.save_as(path=f"videos/{request.node.name}.webm")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def artifacts(request):
    yield
    if request.node.rep_call.failed:
        allure.attach.file(f"screenshots/{request.node.name}.png", name="screenshot",
                           attachment_type=allure.attachment_type.PNG)
        allure.attach.file(f"videos/{request.node.name}.webm", name="video",
                           attachment_type=allure.attachment_type.WEBM)


@pytest.fixture(scope="session", autouse=True)
def clean_folders():
    folders_to_clean = ["generated_files", "downloaded_qr_codes", "reports", "screenshots", "videos"]
    for folder in folders_to_clean:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
    yield
