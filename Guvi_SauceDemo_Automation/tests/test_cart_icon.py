from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Test Case 4 : Verify that cart icon is visible after successful login
def test_cart_icon_visibility(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")

    assert products.is_cart_icon_visible()
    print(products.get_cart_count())