from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    cart_items = (By.CLASS_NAME, "cart_item")
    cart_item_names = (By.CLASS_NAME, "inventory_item_name")
    cart_item_prices = (By.CLASS_NAME, "inventory_item_price")
    checkout_button = (By.ID, "checkout")

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def get_cart_item_count(self):
        return len(self.get_cart_items())

    def get_cart_product_names(self):
        return [
            item.text for item in self.driver.find_elements(*self.cart_item_names)
        ]

    def get_cart_product_prices(self):
        return [
            item.text for item in self.driver.find_elements(*self.cart_item_prices)
        ]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()