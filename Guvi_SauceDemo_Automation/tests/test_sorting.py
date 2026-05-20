from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Test Case 9: Verify product sorting by price (low to high) and name (Z to A)
def test_sort_products_price_low_to_high(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")

    products.sort_by_visible_text("Price (low to high)")

    prices = products.get_all_product_prices()

    assert prices == sorted(prices)



def test_sort_products_name_z_to_a(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")

    products.sort_by_visible_text("Name (Z to A)")

    names = products.get_all_product_names()

    assert names == sorted(names, reverse=True)
