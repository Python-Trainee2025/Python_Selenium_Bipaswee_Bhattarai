from selenium.webdriver.support.wait import WebDriverWait

from page_objects_assignment.cartpom.cartlocators import CartLocators
from page_objects_assignment.cartpom.cartprops import CartPageProperties


class CartPage(CartPageProperties):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remove_item(self):
        self.driver.find_element(*CartLocators.REMOVE_BACKPACK).click()

    def continue_shopping(self):
        self.driver.find_element(*CartLocators.CONTINUE_SHOPPING).click()

