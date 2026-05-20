import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    yield driver
    driver.quit()


def test_guvi_xpath_relative_axes(setup):
    driver = setup
    wait = WebDriverWait(driver, 15)

    xpaths = {
        "Live Classes Parent": "//p[normalize-space()='LIVE Classes']/parent::div",
        "Live Classes First Child": "//p[normalize-space()='LIVE Classes']/parent::div/child::*[1]",
        "Live Classes Preceding Sibling": "//p[normalize-space()='LIVE Classes']/following-sibling::*[local-name()='svg']/preceding-sibling::p",
        "Live Classes Ancestor": "//p[normalize-space()='LIVE Classes']/ancestor::div",
        "Live Classes Following Sibling": "//p[normalize-space()='LIVE Classes']/following-sibling::*[local-name()='svg']",

        "Courses Parent": "//p[normalize-space()='Courses']/parent::div",
        "Courses First Child": "//p[normalize-space()='Courses']/parent::div/child::*[1]",
        "Courses Preceding Sibling": "//p[normalize-space()='Courses']/following-sibling::*[local-name()='svg']/preceding-sibling::p",
        "Courses Ancestor": "//p[normalize-space()='Courses']/ancestor::div",
        "Courses Following Sibling": "//p[normalize-space()='Courses']/following-sibling::*[local-name()='svg']",

        "Practice Parent": "//p[normalize-space()='Practice']/parent::div",
        "Practice First Child": "//p[normalize-space()='Practice']/parent::div/child::*[1]",
        "Practice Preceding Sibling": "//p[normalize-space()='Practice']/following-sibling::*[local-name()='svg']/preceding-sibling::p",
        "Practice Ancestor": "//p[normalize-space()='Practice']/ancestor::div",
        "Practice Following Sibling": "//p[normalize-space()='Practice']/following-sibling::*[local-name()='svg']",
        "Practice Second Sibling": "(//p[normalize-space()='Practice']/parent::div/following-sibling::div)[2]",

        "Resources Parent": "//p[normalize-space()='Resources']/parent::div",
        "Resources First Child": "//p[normalize-space()='Resources']/parent::div/child::*[1]",
        "Resources Preceding Sibling": "//p[normalize-space()='Resources']/following-sibling::*[local-name()='svg']/preceding-sibling::p",
        "Resources Ancestor": "//p[normalize-space()='Resources']/ancestor::div",
        "Resources Following Sibling": "//p[normalize-space()='Resources']/following-sibling::*[local-name()='svg']",
        "Resources Second Sibling": "(//p[normalize-space()='Resources']/parent::div/following-sibling::div)[2]",

        "Our Products Parent": "//p[normalize-space()='Our Products']/parent::div",
        "Our Products First Child": "//p[normalize-space()='Our Products']/parent::div/child::*[1]",
        "Our Products Preceding Sibling": "//p[normalize-space()='Our Products']/following-sibling::*[local-name()='svg']/preceding-sibling::p",
        "Our Products Ancestor": "//p[normalize-space()='Our Products']/ancestor::div",
        "Our Products Following Sibling": "//p[normalize-space()='Our Products']/following-sibling::*[local-name()='svg']",
        "Our Products Second Sibling": "(//p[normalize-space()='Our Products']/parent::div/following-sibling::div)[2]",

        "Login Parent": "(//button[normalize-space()='Login'])[1]/parent::div",
        "Login First Child": "(//button[normalize-space()='Login'])[1]/parent::div/child::*[1]",
        "LoginPreceding Sibling" :"(//button[contains(text(),'Sign up')]/preceding-sibling::button)[1]",
        "Login Ancestor": "// button[ @ id = 'login-btn'] / ancestor::div",
        "Login Following Sibling": "//button[@id='login-btn']/following-sibling::button",

        "Sign Up Parent": "(//button[normalize-space()='Sign up'])[1]/parent::div",
        "Sign Up First Child": "(//button[normalize-space()='Sign up'])[1]/parent::div/child::*[1]",
        "Sign Up Preceding Sibling": "(//button[normalize-space()='Sign up'])[1]/preceding-sibling::button",
        "Sign Up Ancestor": "(//button[normalize-space()='Sign up'])[1]/ancestor::header",
        "Sign Up Following Sibling" : "(//button[@id='login-btn']/following-sibling::button)[1]",
    }

    for name, xpath in xpaths.items():
        elements = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        assert len(elements) > 0, f"{name} XPath not found"
        print(f"{name} XPath found successfully")


def test_click_login_button(setup):
    driver = setup
    wait = WebDriverWait(driver, 15)

    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Login'])[1]"))
    )

    assert login_button.is_displayed()
    print("Login button is visible and clickable")