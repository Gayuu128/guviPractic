from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    summary_items = (By.CLASS_NAME, "cart_item")
    confirmation_message = (By.CLASS_NAME, "complete-header")

    def enter_checkout_details(self, fname, lname, zipcode):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zipcode)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_summary_item_count(self):
        return len(self.driver.find_elements(*self.summary_items))

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_message).text