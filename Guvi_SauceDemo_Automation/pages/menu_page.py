from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")
    reset_button = (By.ID, "reset_sidebar_link")

    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()

    def logout(self):
        self.open_menu()
        self.wait.until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

    def reset_app_state(self):
        self.open_menu()
        self.wait.until(
            EC.element_to_be_clickable(self.reset_button)
        ).click()