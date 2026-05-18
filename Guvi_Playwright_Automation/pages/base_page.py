class BasePage:

    def __init__(self,page):

        self.page=page


    def click(self,locator):

        self.page.locator(locator).click()


    def enter_text(self,locator,text):

        self.page.locator(locator).fill(text)


    def get_text(self,locator):

        return self.page.locator(locator).inner_text()


    def is_visible(self,locator):

        return self.page.locator(locator).is_visible()


    def get_title(self):

        return self.page.title()


    def get_url(self):

        return self.page.url