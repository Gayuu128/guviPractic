from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Test Case 6 : Add 4 randomly selected products to cart and verify cart count
def test_add_selected_products_to_cart(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")

    selected_products = products.select_random_products(4)
    products.add_selected_products_to_cart(selected_products)

    assert products.get_cart_count() == "4"