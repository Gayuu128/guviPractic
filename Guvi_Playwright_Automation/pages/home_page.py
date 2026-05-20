from pages.base_page import BasePage


class HomePage(BasePage):


    LOGIN_BUTTON="(//button[@id='login-btn'])[1]"

    SIGNUP_BUTTON="(//button[contains(text(),'Sign up')])[1]"

    COURSES="//p[contains(@class,'menu-hover') and contains(text(),'Courses')]"

    LIVE_CLASSES="//p[contains(@class,'menu-hover') and contains(text(),'LIVE Classes')]"

    PRACTICE="//p[contains(@class,'menu-hover') and contains(text(),'Practice')]"

    DOBBY="//span[@id='zs_fl_chat']"


    def open_home(self):

        self.page.goto("https://www.guvi.in")


    def click_login(self):

        self.click(self.LOGIN_BUTTON)


    def click_signup(self):

        self.click(self.SIGNUP_BUTTON)