from pages.base_page import BasePage


class DashboardPage(BasePage):


    PROFILE_ICON=(
        "(//img[@alt='Profile'])[1]"
    )

    LOGOUT_BUTTON=(
        "(//p[text()='Sign Out'])[1]"
    )
    LOGIN_BUTTON=(
        "(// button[@ id='login-btn'])[1]"
    )


    def logout(self):

        self.click(
            self.PROFILE_ICON
        )

        self.click(
            self.LOGOUT_BUTTON
        )