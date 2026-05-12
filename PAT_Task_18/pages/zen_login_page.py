from playwright.sync_api import Page, TimeoutError


class ZenLoginPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.username_input = "input[type='text']"

        self.password_input = "input[type='password']"

        self.login_button = "//button[@type='submit']"

        self.profile_icon = (
            "//p[contains(@class,'avatar-profile-name')]"
        )

        self.logout_button = (
            "//div[text()='Log out']"
        )

    # Enter Username
    def enter_username(self, username):

        username_field = self.page.locator(
            self.username_input
        )

        self.page.wait_for_selector(
            self.username_input,
            timeout=60000
        )

        username_field.fill(username)

    # Enter Password
    def enter_password(self, password):

        password_field = self.page.locator(
            self.password_input
        )

        self.page.wait_for_selector(
            self.password_input,
            timeout=60000
        )

        password_field.fill(password)

    # Click Login
    def click_login(self):

        login_btn = self.page.locator(
            self.login_button
        )

        login_btn.wait_for(state="visible")

        login_btn.click()

    # Verify Successful Login
    def is_login_successful(self):

        try:

            self.page.wait_for_url(
                "**/dashboard",
                timeout=30000
            )

            return True

        except TimeoutError:

            return False

    # Open Profile Menu
    def open_profile_menu(self):

        profile = self.page.locator(
            self.profile_icon
        )

        profile.wait_for(state="visible")

        profile.click()

    # Logout
    def click_logout(self):

        logout_btn = self.page.locator(
            self.logout_button
        )

        logout_btn.wait_for(state="visible")

        logout_btn.click()