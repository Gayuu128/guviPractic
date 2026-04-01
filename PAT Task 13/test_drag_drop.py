

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


# Positive Test Case
def test_drag_and_drop_success(driver):
    driver.get("https://jqueryui.com/droppable/")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))

    source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
    target = wait.until(EC.presence_of_element_located((By.ID, "droppable")))

    # Perform Drag and Drop
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()


    assert "Dropped!" in target.text


# Negative Test Case
def test_drag_and_drop_failure(driver):
    driver.get("https://jqueryui.com/droppable/")

    wait = WebDriverWait(driver, 10)


    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))

    # Locate elements
    source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
    target = wait.until(EC.presence_of_element_located((By.ID, "droppable")))


    assert "Dropped!" not in target.text


