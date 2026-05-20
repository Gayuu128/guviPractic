from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AdminUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")

        self.user_role_dropdown = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
        self.status_dropdown = (By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[2]")

        self.employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.employee_suggestion = (By.XPATH, "//div[@role='listbox']//span")

        self.username = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
        self.password = (By.XPATH, "(//input[@type='password'])[1]")
        self.confirm_password = (By.XPATH, "(//input[@type='password'])[2]")

        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")

    def click_admin_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    def select_user_role(self, role):
        self.wait.until(EC.element_to_be_clickable(self.user_role_dropdown)).click()
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{role}']"))
        ).click()

    def enter_employee_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.employee_name)).send_keys(name)

    def select_employee_suggestion(self):
        self.wait.until(EC.visibility_of_element_located(self.employee_suggestion)).click()

    def select_status(self, status):
        self.wait.until(EC.element_to_be_clickable(self.status_dropdown)).click()
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{status}']"))
        ).click()

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def enter_confirm_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.confirm_password)).send_keys(password)

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()