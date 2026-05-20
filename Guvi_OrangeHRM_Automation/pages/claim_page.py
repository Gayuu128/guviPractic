import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ClaimPage:

    submit_claim_menu = (By.XPATH, "//a[text()='Submit Claim']")
    event_dropdown = (By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]")
    currency_dropdown = (By.XPATH, "(//div[contains(@class,'oxd-select-text oxd-select-text--active')])[2]")
    currency_option = (By.XPATH, "(//div[@role='listbox])[2]")
    first_dropdown_option = (By.XPATH, "(//div[@role='option'])[2]")
    remarks_box = (By.XPATH, "//textarea")
    create_button = (By.XPATH, "//button[text()=' Create ']")
    submit_button = (By.XPATH, "//button[contains(.,'Submit')]")
    success_message = (By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]")
    final_claim_submit = (By.XPATH, "//button[text()=' Submit ']")
    back_button = (By.XPATH, "//button[text()=' Back ']")
    my_claim =(By.XPATH, "//h5[text()='My Claims']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_submit_claim(self):
        self.wait.until(
            EC.element_to_be_clickable(self.submit_claim_menu)
        ).click()

    def select_event(self):
        self.wait.until(
            EC.element_to_be_clickable(self.event_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.first_dropdown_option)
        ).click()

    def select_currency(self):
        self.wait.until(
            EC.element_to_be_clickable(self.currency_dropdown)
        ).click()
        time.sleep(5)

        self.wait.until(
            EC.element_to_be_clickable(self.first_dropdown_option)
        ).click()

    def enter_remarks(self, reason):
        self.wait.until(
            EC.visibility_of_element_located(self.remarks_box)
        ).send_keys(reason)

    def click_create(self):
        self.wait.until(
            EC.element_to_be_clickable(self.create_button)
        ).click()
        time.sleep(5)

    def submit_claim(self):
        self.wait.until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()
    def final_submit(self):
        self.wait.until(
            EC.element_to_be_clickable(self.final_claim_submit)
        ).click()
    def click_back(self):
        self.wait.until(
            EC.element_to_be_clickable(self.back_button)
        ).click()
        self.wait.until(
            EC.visibility_of_element_located(self.my_claim)
        ).is_displayed()

    def is_success_message_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.success_message)
            ).is_displayed()
        except Exception:
            return False