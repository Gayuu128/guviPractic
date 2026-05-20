from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyInfoPage:

    sub_menus = {
        "Personal Details": (By.XPATH, "//a[text()='Personal Details']"),
        "Contact Details": (By.XPATH, "//a[text()='Contact Details']"),
        "Emergency Contacts": (By.XPATH, "//a[text()='Emergency Contacts']"),
        "Dependents": (By.XPATH, "//a[text()='Dependents']"),
        "Immigration": (By.XPATH, "//a[text()='Immigration']"),
        "Job": (By.XPATH, "//a[text()='Job']"),
        "Salary": (By.XPATH, "//a[text()='Salary']")
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_submenu_clickable(self, submenu_name):
        element = self.wait.until(
            EC.element_to_be_clickable(self.sub_menus[submenu_name])
        )
        return element.is_displayed() and element.is_enabled()