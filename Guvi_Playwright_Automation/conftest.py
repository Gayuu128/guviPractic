import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_setup():

    playwright = sync_playwright().start()

    # Launch Microsoft Edge
    browser = playwright.chromium.launch(
        channel="msedge",
        headless=False
    )

    page = browser.new_page()

    yield page

    page.close()
    browser.close()
    playwright.stop()