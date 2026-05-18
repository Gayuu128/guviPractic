from pages.base_page import BasePage
from pages.home_page import HomePage


class LoginPage(BasePage):


    EMAIL="#email"

    PASSWORD="#password"

    LOGIN_BUTON="//a[@id='login-btn']"

    ERROR_MESSAGE="//div[@class='invalid-feedback is-invalid']"
    COURSES = "//p[contains(@class,'menu-hover') and contains(text(),'Courses')]"


    def login(self,email,password):

        self.enter_text(
            self.EMAIL,
            email
        )

        self.enter_text(
            self.PASSWORD,
            password
        )

        self.click(self.LOGIN_BUTON)