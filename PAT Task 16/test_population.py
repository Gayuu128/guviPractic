import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from population import PopulationPage


@pytest.fixture
def setup():
    """
    Setup browser instance
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_population_counter(setup):
    """
    Test to continuously print population count until CTRL+C
    """
    driver = setup

    driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")

    population_page = PopulationPage(driver)

    print("\nPress CTRL+C to stop...\n")

    try:
        while True:
            population = population_page.get_population()
            print("Current Population:", population)
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user (CTRL+C)")