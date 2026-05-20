from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

# Test Case 7 : Verify that products added to cart match the selected products
def test_validate_product_details_inside_cart(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    login.login("standard_user", "secret_sauce")

    selected_products = products.select_random_products(4)
    selected_data = products.add_selected_products_to_cart(selected_products)

    expected_names = [item["name"] for item in selected_data]

    products.click_cart_icon()

    actual_names = cart.get_cart_product_names()

    assert cart.get_cart_item_count() == 4
    assert sorted(actual_names) == sorted(expected_names)