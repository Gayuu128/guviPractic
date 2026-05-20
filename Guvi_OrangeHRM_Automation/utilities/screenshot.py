import datetime


class Screenshot:

    @staticmethod
    def capture(driver, name):
        time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        driver.save_screenshot(f"screenshots/{name}_{time}.png")