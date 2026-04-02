from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # FIXED XPATH
        self.population_value = (By.XPATH, "//div[@class='counter-ticker is-size-2-mobile']")

    def get_population(self):
        """
        Fetch the current population value using Explicit Wait
        """
        element = self.wait.until(
            EC.visibility_of_element_located(self.population_value)
        )
        return element.text.strip()