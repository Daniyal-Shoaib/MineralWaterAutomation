import pytest
from playwright.sync_api import Playwright, sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture()
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    
@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)

