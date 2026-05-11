import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def setup():

    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(
            headless=False
        )

        # Create browser context
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Navigate to Zen Portal
        page.goto("https://www.zenclass.in/login")

        yield page

        # Close browser
        browser.close()