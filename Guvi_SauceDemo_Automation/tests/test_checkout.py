from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

# Test Case 8 : Perform checkout by entering user details and completing order
def test_complete_checkout_and_validate_order(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login("standard_user", "secret_sauce")

    selected_products = products.select_random_products(4)
    products.add_selected_products_to_cart(selected_products)

    products.click_cart_icon()
    cart.click_checkout()

    checkout.enter_checkout_details("Gayathri", "Anand", "600001")
    checkout.click_continue()

    assert checkout.get_summary_item_count() == 4

    driver.save_screenshot("screenshots/order_summary.png")

    checkout.click_finish()

    message = checkout.get_confirmation_message()

    assert "thank you" in message.lower()