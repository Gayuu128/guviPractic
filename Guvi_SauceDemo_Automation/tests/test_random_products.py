from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Test Case 5 : Randomly select 4 products and extract their names and prices
def test_random_product_selection_and_data_extraction(setup):

    driver = setup
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.login("standard_user", "secret_sauce")

    selected_products = products.select_random_products(4)

    selected_data = []

    for product in selected_products:
        name = products.get_product_name_from_item(product)
        price = products.get_product_price_from_item(product)

        selected_data.append({
            "name": name,
            "price": price
        })

    print("Selected Products:", selected_data)

    assert len(selected_data) == 4