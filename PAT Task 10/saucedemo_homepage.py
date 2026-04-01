"""
SauceDemo - Python Selenium code for performing automation
"""

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Create class
class SauceDemoHome:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        """Launch the website"""
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except:
            print("Error: Unable to start automation")
            return False

    def login(self):
        """Perform login"""
        try:
            self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
            self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()
            return True
        except:
            print("Error: Login failed")
            return False

    def fetch_title(self):
        """Fetch title of webpage"""
        return self.driver.title

    def fetch_url(self):
        """Fetch current URL"""
        return self.driver.current_url

    def fetch_dashboard_url(self):
        """Fetch dashboard URL after login"""
        return self.driver.current_url

    def save_page_content(self):
        """Save entire webpage content to text file"""
        try:
            content = self.driver.page_source
            with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
                file.write(content)
            print("Webpage content saved successfully!")
            return True
        except:
            print("Error saving webpage content")
            return False

    def shutdown(self):
        """Close browser"""
        self.driver.quit()