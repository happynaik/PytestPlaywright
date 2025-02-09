import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def test_mac(browser):
    browser.goto("https://www.apple.com/")
    browser.wait_for_selector("a[aria-label='Mac']", timeout=20000)
    browser.click("a[aria-label='Mac']")
    print("Clicked Mac")
    browser.wait_for_selector(".chapternav-items", timeout=20000)
    assert browser.is_visible(".chapternav-items"), "Chapter Nav Items not visible"
    menuitems = browser.locator(".chapternav-label").all_text_contents()
    print("All Menu Items Under Mac:", menuitems)

    assert "Mac Studio" in menuitems, "Accessories not found in menuItems"

    alllinkselements = browser.locator("//a").all()

    for link in alllinkselements:
        text = link.text_content().strip()
        print("Extracted link text", text)

        if text == "MacAAA":
            assert True, "Mac menu item found"
