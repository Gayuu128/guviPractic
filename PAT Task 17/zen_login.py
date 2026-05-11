from playwright.sync_api import Page, TimeoutError


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.username_input = "//input[@type='text']"

        self.password_input = "//input[@type='password']"

        self.login_button = "//button[@type='submit']"

        self.profile_icon = (
            "//p[contains(@class,'avatar-profile-name')]")

        self.logout_button = (
            "//div[text()='Log out']")

        self.popup =(
            "//button[@class='custom-close-button']")

    # Enter Username
    def enter_username(self, username_text):

        username = self.page.locator(
            self.username_input
        )

        username.wait_for(state="visible")

        username.fill(username_text)

    # Enter Password
    def enter_password(self, password_text):

        password = self.page.locator(
            self.password_input
        )

        password.wait_for(state="visible")

        password.fill(password_text)

    # Click Login Button
    def click_login(self):

        login_btn = self.page.locator(
            self.login_button
        )

        login_btn.wait_for(state="visible")

        login_btn.click()

    # Validate Successful Login
    def is_login_successful(self):

        try:

            self.page.wait_for_url(
                "**/dashboard",
                timeout=20000
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

    def close_popup(self):
         popup_close= self.page.locator(
            self.popup
        )

         popup_close.wait_for(state="visible")

         popup_close.click()

    # Click Logout
    def click_logout(self):

        logout_btn = self.page.locator(
            self.logout_button
        )

        logout_btn.wait_for(state="visible")

        logout_btn.click()