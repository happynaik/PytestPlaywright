import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_login(browser):
    browser.goto("https://www.apple.com/")
    browser.click("#globalnav-menubutton-link-bag")
    browser.wait_for_selector("a[data-analytics-title='signIn']", timeout=5000)
    assert browser.is_visible("a[data-analytics-title='signIn']"), "Sign In Link not visible"
    browser.click("a[data-analytics-title='signIn']")

    print("Clicked SignIn")
