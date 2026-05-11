import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

        '''self.username = (By.XPATH, "//input[@id=':r1:']")
           self.password = (By.XPATH, "//input[@id=':r2:']")
           self.login_btn = (By.XPATH, "//button[@type='submit']")
           self.logout_btn = (By.XPATH, "//div[text()='Log out']")
           self.error_msg = (By.XPATH, "//input[@id=':r2:'][aria-invalid='true']")'''