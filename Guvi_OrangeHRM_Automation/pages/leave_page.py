import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LeavePage:
    assign_leave_menu = (By.XPATH, "//a[text()='Assign Leave']")
    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_suggestion = (By.XPATH, "(//div[@role='listbox'])[1]")

    leave_type_dropdown = (By.XPATH, "//label[text()='Leave Type']/following::div[1]")
    leave_type_option = (By.XPATH, "//span[text()='CAN - FMLA']")

    from_date = (By.XPATH, "//label[text()='From Date']/following::input[1]")
    to_date = (By.XPATH, "//label[text()='To Date']/following::input[1]")

    assign_button = (By.XPATH, "//button[text()=' Assign ']")
    confirm_button = (By.XPATH, "//button[text()=' Ok ']")
    success_message = (By.XPATH, "")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_assign_leave(self):

        self.wait.until(
            EC.element_to_be_clickable(self.assign_leave_menu)
        ).click()

    def enter_employee_name(self, name):
        field = self.wait.until(
            EC.visibility_of_element_located(self.employee_name)
        )
        field.send_keys(name)
        time.sleep(3)


        # select suggestion
        self.wait.until(
            EC.element_to_be_clickable(self.employee_suggestion)
        ).click()


    def select_leave_type(self):
        self.wait.until(
            EC.element_to_be_clickable(self.leave_type_dropdown)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.leave_type_option)
        ).click()

    def select_dates(self):
        self.wait.until(
            EC.element_to_be_clickable(self.from_date)
        ).send_keys("20-05-2026")
        self.wait.until(
            EC.element_to_be_clickable(self.to_date)
        )


    def click_assign(self):
        self.wait.until(
            EC.element_to_be_clickable(self.assign_button)
        ).click()
        button = self.wait.until(
            EC.element_to_be_clickable(self.assign_button)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        button.click()
        time.sleep(3)
        self.wait.until(
            EC.element_to_be_clickable(self.confirm_button)
        ).click()
        time.sleep(3)
