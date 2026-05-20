from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.menu_page import MenuPage

# Test Case 10 : Verify that resetting app state clears cart and restores default state
def test_reset_app_state_functionality(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)
    menu = MenuPage(driver)

    login.login("standard_user", "secret_sauce")

    selected_products = products.select_random_products(4)
    products.add_selected_products_to_cart(selected_products)

    assert products.get_cart_count() == "4"

    menu.reset_app_state()

    driver.refresh()


    assert products.get_cart_count() == "0"