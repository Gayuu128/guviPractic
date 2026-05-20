from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    inventory_items = (By.CLASS_NAME, "inventory_item")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    product_prices = (By.CLASS_NAME, "inventory_item_price")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def is_cart_icon_visible(self):
        return self.driver.find_element(*self.cart_icon).is_displayed()

    def get_all_products(self):
        return self.driver.find_elements(*self.inventory_items)

    def select_random_products(self, count=4):
        products = self.get_all_products()
        return random.sample(products, count)

    def get_product_name_from_item(self, item):
        return item.find_element(By.CLASS_NAME, "inventory_item_name").text

    def get_product_price_from_item(self, item):
        return item.find_element(By.CLASS_NAME, "inventory_item_price").text

    def add_selected_products_to_cart(self, selected_products):
        selected_data = []

        for product in selected_products:
            name = self.get_product_name_from_item(product)
            price = self.get_product_price_from_item(product)

            product.find_element(By.TAG_NAME, "button").click()

            selected_data.append({
                "name": name,
                "price": price
            })

        return selected_data

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.cart_badge)

        if len(badges) == 0:
            return "0"

        return badges[0].text

    def click_cart_icon(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_all_product_names(self):
        return [
            item.text for item in self.driver.find_elements(*self.product_names)
        ]

    def get_all_product_prices(self):
        prices = self.driver.find_elements(*self.product_prices)

        return [
            float(price.text.replace("$", "")) for price in prices
        ]

    def sort_by_visible_text(self, text):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text(text)