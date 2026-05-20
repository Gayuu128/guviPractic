from pages.home_page import HomePage

from utils.test_data import TestData

# Test Case 1 : Verify whether the GUVI URL is valid.
def test_url(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()


    assert page.url==(
        TestData.BASE_URL+"/"
    )

# Test Case 2 : Verify whether the title of the GUVI webpage is correct.
def test_title(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()


    assert page.title()==(
        TestData.TITLE
    )

# Test Case 8 : Verify key menu items are displayed.
def test_menu_items(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()


    assert home.is_visible(
        home.COURSES
    )



# Test Case 9 : Validate Dobby GUVI Assistant presence.
def test_dobby(browser_setup):


    page=browser_setup

    home=HomePage(page)

    home.open_home()
    page.wait_for_selector(
        home.DOBBY
    )

    assert home.is_visible(
        home.DOBBY
    )