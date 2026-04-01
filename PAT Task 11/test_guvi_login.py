
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.guvi.in/"

# -------------------------------
# Test 1: Validate Login Button URL
# -------------------------------
def test_validate_login_url(setup):
    driver = setup
    driver.get(URL)
    print(URL)

    login_btn = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_btn.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("sign-in")
    )

    assert "https://www.guvi.in/sign-in/" in driver.current_url


# -------------------------------
# Test 2: Validate Input Fields
# -------------------------------
def test_validate_input_fields(setup):
    driver = setup
    driver.get(URL)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    password = driver.find_element(By.ID, "password")

    assert username.is_displayed() and username.is_enabled()
    assert password.is_displayed() and password.is_enabled()


# -------------------------------
# Test 3: Positive Login Test
# -------------------------------
def test_positive_login(setup):
    driver = setup
    driver.get(URL)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    driver.find_element(By.ID, "email").send_keys("validemail@gmail.com")
    driver.find_element(By.ID, "password").send_keys("validpassword")

    driver.find_element(By.XPATH, "//a[@id='login-btn']").click()

    print("Current URL:", driver.current_url)

    # Wait for successful login
    WebDriverWait(driver, 8).until(
        EC.url_changes("https://www.guvi.in/sign-in/")
    )

    assert driver.find_element(By.XPATH, "//p[text()='LIVE Classes']").is_displayed()


# -------------------------------
# Test 4: Negative Login Test
# -------------------------------
def test_negative_login(setup):
    driver = setup
    driver.get(URL)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    driver.find_element(By.ID, "email").send_keys("invalid@gmail.com")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")

    driver.find_element(By.XPATH, "//a[@id='login-btn']").click()

    # Check error message
    error_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "invalid-feedback"))
    )

    assert error_msg.is_displayed()


# -------------------------------
# Test 5: Validate Submit Button
# -------------------------------
def test_submit_button(setup):
    driver = setup
    driver.get(URL)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@id='login-btn']"))
    )

    assert submit_btn.is_enabled()